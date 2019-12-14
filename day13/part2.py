from collections import defaultdict
import queue

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
        self.__output_queue = queue.Queue(maxsize=1)
        self.__output_list = []
        self.__halt = False
        self.__initialized = False
        self.__needs_input = False
        self.__error = False

    def input(self, v):
        self.run(v)

    def output(self):
        return self.out

    def output_queue(self):
        return self.__output_queue

    def needs_input(self):
        return self.__needs_input

    def output_list(self):
        return self.__output_list

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
            v1 = p1 if m1 == 1 else self.memory[o1+p1]
            v2 = p2 if m2 == 1 else self.memory[o2+p2]
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
                if input == None:
                    self.__needs_input = True
                    break
                self.memory[o1+p1] = input
                input = None
                self.__needs_input = False
                self.pointer += 2
            elif operation == 4:
                self.pointer += 2
                self.__output_queue.put(v1)
                self.out = v1
                return v1
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

def find_pad_and_ball(board):
    for y in range(21):
        for x in range(44):
            item = board.get((x,y),0)
            if item == 4:
                ball=x
            if item == 3:
                return x, ball

def show_board(board):
    for y in range(21):
        print(''.join([' #*=o'[board.get((x, y), 0)] for x in range(44)]))

mreset = []
for l in open('input.txt', 'r'):
    mreset = [int(x) for x in l.strip().split(',')]
mreset[0] = 2
m = Machine(mreset)
board = {}
score = 0
previous_score = 0
while not m.halted():
    if m.needs_input():
        if score-previous_score > 100:
            show_board(board)
            print(score)
            previous_score = score
        pad, ball = find_pad_and_ball(board)
        m.input(1 if pad < ball else (-1 if pad > ball else 0))
    elif m.output_queue().full():
        x = m.output_queue().get()
        m.run()
        y = m.output_queue().get()
        m.run()
        if x == -1 and y == 0:
            score = m.output_queue().get()
        else:
            board[(x,y)] = m.output_queue().get()
    elif m.halted():
        print('exiting')
        break
    else:
        m.run()
show_board(board)
print(score)