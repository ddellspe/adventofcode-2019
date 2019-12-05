import math

array = None
with open('input.txt', 'r') as file:
  inp = file.readline()
  array = [int(val) for val in inp.split(',')]
start = 0
operation = 0
while operation != 99:
  operation_pattern = array[start]
  operation = int(operation_pattern%100)
  pos1_mode = int(operation_pattern/100)%10
  pos2_mode = int(operation_pattern/1000)%10
  pos3_mode = int(operation_pattern/10000)%10
  if operation == 99:
    print('found halt code, exiting')
    break
  elif operation == 1:
    pos1 = array[start+1]
    value1 = array[pos1] if pos1_mode == 0 else pos1
    pos2 = array[start+2]
    value2 = array[pos2] if pos2_mode == 0 else pos2
    sto = array[start+3]
    array[sto] = value1 + value2
    start += 4
  elif operation == 2:
    pos1 = array[start+1]
    value1 = array[pos1] if pos1_mode == 0 else pos1
    pos2 = array[start+2]
    value2 = array[pos2] if pos2_mode == 0 else pos2
    sto = array[start+3]
    array[sto] = value1 * value2
    start += 4
  elif operation == 3:
    sto = array[start+1]
    number = int(input('Enter your value: '))
    array[sto] = number
    start += 2
  elif operation == 4:
    read = array[start+1]
    print(array[read] if pos1_mode == 0 else read)
    start += 2
  elif operation == 5:
    pos1 = array[start+1]
    value1 = array[pos1] if pos1_mode == 0 else pos1
    pos2 = array[start+2]
    value2 = array[pos2] if pos2_mode == 0 else pos2
    if value1 != 0:
      start = value2
    else:
      start += 3
  elif operation == 6:
    pos1 = array[start+1]
    value1 = array[pos1] if pos1_mode == 0 else pos1
    pos2 = array[start+2]
    value2 = array[pos2] if pos2_mode == 0 else pos2
    if value1 == 0:
      start = value2
    else:
      start += 3
  elif operation == 7:
    pos1 = array[start+1]
    value1 = array[pos1] if pos1_mode == 0 else pos1
    pos2 = array[start+2]
    value2 = array[pos2] if pos2_mode == 0 else pos2
    pos3 = array[start+3]
    value3 = pos3
    if value1 < value2:
      array[value3] = 1
    else:
      array[value3] = 0
    start += 4
  elif operation == 8:
    pos1 = array[start+1]
    value1 = array[pos1] if pos1_mode == 0 else pos1
    pos2 = array[start+2]
    value2 = array[pos2] if pos2_mode == 0 else pos2
    pos3 = array[start+3]
    value3 = pos3
    if value1 == value2:
      array[value3] = 1
    else:
      array[value3] = 0
    start += 4
  else:
    print('something went wrong at position: ' + str(start) + ' encountered at: ' + str(operation))
    print(array)
    exit(-1)
print(array[0])