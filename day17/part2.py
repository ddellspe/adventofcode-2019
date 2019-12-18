from collections import defaultdict, deque
import queue

def detect_intersections(image):
    robot_loc = (0, 0)
    sum = 0
    for row in range(len(image)):
        for col in range(len(image[row])):
            #skip if at the extremes
            if image[row][col] in ['^', 'v', '<', '>']:
                robot_loc = (col, row)
            if row == 0 or row == len(image)-1 or col == 0 or col == len(image[row])-1:
                continue

            if image[row][col] == '#':
                if image[row - 1][col] == '#' and image[row + 1][col] == '#' and image[row][col + 1] == '#' and image[row][col - 1] == '#':
                    sum += row*col
    return sum, robot_loc

class Machine(object):
    def __init__(self, mem=None, mem_map=None):
        if mem_map:
            self.memory = mem_map
        else:
            self.memory = defaultdict(lambda: 0, enumerate(mem))
        self.pointer = 0
        self.len = len(self.memory)
        self.out = 0
        self.relative_location = 0
        self.__output_list = []
        self.__halt = False
        self.__needs_input = False
        self.__error = False

    def input(self, v):
        return self.run(v)

    def output(self):
        return self.out

    def needs_input(self):
        return self.__needs_input

    def output_list(self):
        return self.__output_list

    def halted(self):
        return self.__halt

    def errored(self):
        return self.__error

    def run(self, input=None):
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
                return None
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
                self.out = v1
                self.__output_list.append(v1)
                #return v1
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
    mreset = [int(row) for row in l.strip().split(',')]
m = Machine(mreset[:])
m.run()
print(m.needs_input(), m.halted())
image = []
image_row = []
for character in m.output_list():
    if character == 10:
        if len(image_row) > 0:
            image.append(image_row[:])
            image_row = []
        continue
    image_row.append(chr(character))
if len(image_row) > 0:
    image.append(image_row[:])
sum, robot_loc = detect_intersections(image)
for row in image:
    print("".join(row))
height, width = len(image), len(image[0])
print(sum)
print(robot_loc, (width, height))
print(image[robot_loc[0]][robot_loc[1]])

mreset[0] = 2
m2 = Machine(mreset[:])