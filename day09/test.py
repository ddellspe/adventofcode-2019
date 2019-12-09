import sys
import collections
# usage pyhon3 9.1.py program input
 
def run(inp):
    initmem = list(map(int, open(sys.argv[1]).read().split(',')))
    mem = collections.defaultdict(lambda: 0, enumerate(initmem))
    pc,base = 0, 0
    while mem[pc] != 99:
        opcode = mem[pc] % 100
        modes = ("%05d" % mem[pc])[0:3]
        o1 = base if modes[2] == '2' else 0
        o2 = base if modes[1] == '2' else 0
        o3 = base if modes[0] == '2' else 0
        if opcode in (1,2,3,4,5,6,7,8,9):
            op1 = mem[pc+1] if modes[2] == '1' else mem[o1+mem[pc+1]]
        if opcode in (1,2,5,6,7,8):
            op2 = mem[pc+2] if modes[1] == '1' else mem[o2+mem[pc+2]]
        if opcode == 1: # add
            print('adding', op1, 'and', op2, 'storing at position', o3+mem[pc+3])
            mem[o3+mem[pc+3]] = op1+op2
            pc += 4
        elif opcode == 2: # mul
            print('multiplying', op1, 'and', op2, 'storing at position', o3+mem[pc+3])
            mem[o3+mem[pc+3]] = op1*op2
            pc += 4
        elif opcode == 3: # input
            inpt = inp.pop(0)
            print('taking value', inpt, 'storing at', o1+mem[pc+1])
            mem[o1+mem[pc+1]] = inpt
            pc += 2
        elif opcode  == 4: # output
            print('outputing value', op1)
            pc += 2
            yield op1
        elif opcode == 5: # jump if true
            print('moving pointer to', op2, 'if', op1, 'is not equal to 0')
            pc = op2 if op1 != 0 else pc+3
        elif opcode == 6: # jump if false
            print('moving pointer to', op2, 'if', op1, 'is equal to 0')
            pc = op2 if op1 == 0 else pc+3
        elif opcode == 7: # less than
            print('checking if', op1, 'is less than', op2, 'storing at', o3+mem[pc+3])
            mem[o3+mem[pc+3]] = 1 if op1 < op2 else 0
            pc += 4
        elif opcode == 8: # equals
            print('checking if', op1, 'is equal to', op2, 'storing at', o3+mem[pc+3])
            mem[o3+mem[pc+3]] = 1 if op1 == op2 else 0
            pc += 4
        elif opcode == 9: # set relative base
            print('moving relative_location from', base, 'to', base + op1)
            base += op1
            pc += 2
        else: raise Exception("invalid opcode %d" % opcode)
 
for out in run([int(sys.argv[2])]):
    print(out)