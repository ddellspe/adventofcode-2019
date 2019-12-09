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
            o1 = self.relative_location if m1 == 2 else 0
            o2 = self.relative_location if m2 == 2 else 0
            o3 = self.relative_location if m3 == 2 else 0
            p1, p2, p3 = self.memory[self.pointer + 1], self.memory[self.pointer + 2], self.memory[self.pointer + 3]
            # print('op_code', op_code, p1, p2, p3, self.relative_location)
            # print('modes', m1, m2, m3)
            v1 = p1 if m1 == 1 else self.memory[o1+p1]
            v2 = p2 if m2 == 1 else self.memory[o2+p2]
            # print('values', v1, v2, v3)
            if operation == 99:
                self.__halt = True
                print('Halting')
                break
            elif operation == 1:
                self.memory[o3+p3] = v1 + v2
                self.pointer += 4
            elif operation == 2:
                self.memory[o3+p3] = v1 * v2
                self.pointer += 4
            elif operation == 3:
                self.memory[o1+p1] = input
                self.pointer += 2
            elif operation == 4:
                self.out = v1
                print(v1)
                self.pointer += 2
            elif operation == 5:
                self.pointer = v2 if v1 != 0 else self.pointer + 3
            elif operation == 6:
                self.pointer = v2 if v1 == 0 else self.pointer + 3
            elif operation == 7:
                self.memory[o3+p3] = 1 if v1 < v2 else 0
                self.pointer += 4
            elif operation == 8:
                self.memory[o3+p3] = 1 if v1 == v2 else 0
                self.pointer += 4
            elif operation == 9:
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
m.input(2)