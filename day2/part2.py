import math

original_array = None
with open('input.txt', 'r') as file:
  input = file.readline()
  original_array = [int(val) for val in input.split(',')]

for noun in range(100):
  for verb in range(100):
    array = original_array.copy()
    array[1] = noun
    array[2] = verb
    op_count = math.ceil(len(array)/4)
    for position in range(op_count):
      start = position*4
      operation = array[start]
      if operation == 99:
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
        print('something went wrong at position: ' + str(start) + ' encountered at: ' + str(operation))
        print(array)
        array[start+4] = 99
    if array[0] == 19690720:
      print('found noun and verb')
      print('noun is ' + str(noun))
      print('verb is ' + str(verb))
      print('puzzle answer is ' + str(noun*100 + verb))
      exit(0)