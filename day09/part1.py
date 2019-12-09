from collections import defaultdict

import math
import itertools

class Machine(object):
    def __init__(self, mem):
        self.memory = defaultdict(lambda: 0, enumerate(mem))
        self.mem_len = len(mem)
        self.pointer = 0
        self.len = len(mem)
        self.out = 0
        self.relative_location = 0
        self.__halt = False
        self.__initialized = False
        self.__error = False

    def input(self, v):
        self.run(v)

    def output(self):
        return self.out

    def halted(self):
        return self.__halt

    def initialized(self):
        return self.__initialized

    def errored(self):
        return self.__error

    def run(self, input=None):
        if input != None:
            self.__initialized = True
        while self.pointer < self.len:
            op_code = self.memory[self.pointer]
            operation = op_code % 100
            m1 = op_code // 100 % 10
            m2 = op_code // 1000 % 10
            m3 = op_code // 10000 % 10
            p1, p2, p3 = self.memory[self.pointer + 1], self.memory[self.pointer + 2], self.memory[self.pointer + 3]
            #print('op_code', op_code, p1, p2, p3, self.relative_location)
            #print('modes', m1, m2, m3)
            v1 = self.memory[p1] if m1 == 0 else (self.memory[self.relative_location + p1] if m1 == 2 else p1)
            v2 = self.memory[p2] if m2 == 0 else (self.memory[self.relative_location + p2] if m2 == 2 else p2)
            v3 = p3 if m3 == 0 and operation in {1, 2, 7, 8} else self.pointer + 3
            #print('values', p1, p2, p3)
            if operation == 99:
                self.__halt = True
                print('Halting')
                break
            elif operation == 1:
                print('adding', v1, 'and', v2, 'storing at', v3)
                self.memory[v3] = v1 + v2
                self.pointer += 4
            elif operation == 2:
                print('multiplying', v1, 'and', v2, 'storing at', v3)
                self.memory[v3] = v1 * v2
                self.pointer += 4
            elif operation == 3:
                print('taking value', input, 'storing at', v1)
                self.memory[p1 + self.relative_location if m1 == 2 else 0] = input
                self.pointer += 2
            elif operation == 4:
                print('outputing value', v1)
                self.out = v1
                print(' ', self.out)
                self.pointer += 2
            elif operation == 5:
                print('moving pointer to', v2, 'if', v1, 'is not equal to 0')
                self.pointer = v2 if v1 != 0 else self.pointer + 3
            elif operation == 6:
                print('moving pointer to', v2, 'if', v1, 'is equal to 0')
                self.pointer = v2 if v1 == 0 else self.pointer + 3
            elif operation == 7:
                print('checking if', v1, 'is less than', v2, 'storing at', p3 + self.relative_location if m3 == 2 else 0)
                self.memory[p3 + self.relative_location if m3 == 2 else 0] = 1 if v1 < v2 else 0
                self.pointer += 4
            elif operation == 8:
                print('checking if', v1, 'is equal to', v2, 'storing at', p3 + self.relative_location if m3 == 2 else 0)
                self.memory[p3 + self.relative_location if m3 == 2 else 0] = 1 if v1 == v2 else 0
                self.pointer += 4
            elif operation == 9:
                print('moving relative_location from', self.relative_location, 'to', self.relative_location + v1)
                self.relative_location += v1
                self.pointer += 2
            else:
                print("ERROR", self.pointer, operation, [op_code, p1, p2, p3])
                self.__error = True
                break

mreset = []
for l in open('input.txt', 'r'):
    mreset = [int(x) for x in l.strip().split(',')]
m = Machine(mreset)
m.input(1)
#print(dict(m.memory_dict))