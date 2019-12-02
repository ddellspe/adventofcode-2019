import math

array = None
with open('input.txt', 'r') as file:
  input = file.readline()
  array = [int(val) for val in input.split(',')]

op_count = math.ceil(len(array)/4)
array[1] = 12
array[2] = 2
for position in range(op_count):
  start = position*4
  operation = array[start]
  if operation == 99:
    print('found halt code, exiting')
    break
  elif operation == 1:
    pos1 = array[start+1]
    pos2 = array[start+2]
    sto = array[start+3]
    array[sto] = array[pos1]+array[pos2]
  elif operation == 2:
    pos1 = array[start+1]
    pos2 = array[start+2]
    sto = array[start+3]
    array[sto] = array[pos1]*array[pos2]
  else:
    print('something went wrong at position: ' + str(start) + ' encountered a: ' + str(operation))
    print(array)
    exit(-1)
print(array[0])