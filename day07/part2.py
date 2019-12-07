import math
import itertools

class Machine(object):
    def __init__(self, mem):
        self.memory = mem
        self.pointer = 0
        self.len = len(mem)
        self.out = 0
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
            if self.len - self.pointer < 5:
                instr = self.memory + ([0] * 5)
            else:
                instr = self.memory[:self.pointer + 5]
            op_code = self.memory[self.pointer]
            operation = op_code % 100
            m1 = op_code // 100 % 10
            m2 = op_code // 1000 % 10
            m3 = op_code // 10000 % 10
            p1, p2, p3 = instr[self.pointer + 1], instr[self.pointer + 2], instr[self.pointer + 3]
            v1 = self.memory[p1] if m1 == 0 and operation != 99 else p1
            v2 = self.memory[p2] if m2 == 0 and operation not in {99, 3, 4} else p2
            v3 = p3 if m3 == 0 and operation in {1, 2, 7, 8} else self.pointer + 3
            if operation == 99:
                self.__halt = True
                break
            elif operation == 1:
                self.memory[v3] = v1 + v2
                self.pointer += 4
            elif operation == 2:
                self.memory[v3] = v1 * v2
                self.pointer += 4
            elif operation == 3:
                if input == None:
                    break
                self.memory[p1] = input
                input = None
                self.pointer += 2
            elif operation == 4:
                self.out = v1
                self.pointer += 2
            elif operation == 5:
                self.pointer = v2 if v1 != 0 else self.pointer + 3
            elif operation == 6:
                self.pointer = v2 if v1 == 0 else self.pointer + 3
            elif operation == 7:
                self.memory[v3] = 1 if v1 < v2 else 0
                self.pointer += 4
            elif operation == 8:
                self.memory[v3] = 1 if v1 == v2 else 0
                self.pointer += 4
            else:
                print("ERROR", self.pointer, operation, self.memory[self.pointer:self.pointer + 4])
                self.__error = True
                break
def run(data, settings):
    result, perms = 0, list(itertools.permutations(settings,5))
    for p in perms:
        m = [
            Machine(data.copy()),
            Machine(data.copy()),
            Machine(data.copy()),
            Machine(data.copy()),
            Machine(data.copy())
        ]

        current, prev = 0, 4
        while True:
            if m[current].halted() or m[current].errored():
                break
            m[current].run(p[current] if not m[current].initialized() else m[prev].output())
            prev = current
            current = (current + 1) % 5
        result = m[4].output() if m[4].output() > result else result
    return result

mreset = []
for l in open('input.txt', 'r'):
    mreset = [int(x) for x in l.strip().split(',')]

settings = list(range(5, 10))
max = run(mreset, settings)
print("Maximum Thrust: ", max)