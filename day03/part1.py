import math

wire_1_path = None
wire_2_path = None

def print_grid(grid):
  for row in grid:
    print(''.join(row))

def get_max_dimensions(moves):
  col = [0]
  row = [0]
  x = 0
  y = 0
  for move in moves:
    dir = move[0]
    amount = int(move[1:])
    if dir == 'R':
      x += amount
    elif dir == 'L':
      x -= amount
    elif dir == 'U':
      y -= amount
    elif dir == 'D':
      y += amount
    row.append(y)
    col.append(x)
  return min(row), max(row), min(col), max(col)

def generate_grid(row_size, col_size, row_origin, col_origin):
  grid = []
  for row in range(row_size):
    grid_row = []
    for col in range(col_size):
      grid_row.append('O' if row == row_origin and col == col_origin else '.')
    grid.append(grid_row)
  return grid

def navigate_grid(grid, path, row_origin, col_origin):
  row = row_origin
  col = col_origin
  for move in path:
    if row != row_origin or col != col_origin:
      grid[row][col] = '+'
    dir = move[0]
    amount = int(move[1:])
    if dir == 'R':
      for step in range(amount):
        col+=1
        grid[row][col] = '-'
    elif dir == 'L':
      for step in range(amount):
        col-=1
        grid[row][col] = '-'
    elif dir == 'U':
      for step in range(amount):
        row-=1
        grid[row][col] = '|'
    elif dir == 'D':
      for step in range(amount):
        row+=1
        grid[row][col] = '|'

def generate_full_grid(wire_1, wire_2, full):
  for row_num, row in enumerate(wire_1):
    for col_num, w1_val in enumerate(row):
      w2_val = wire_2[row_num][col_num]
      if w1_val == '.':
        full[row_num][col_num] = w2_val
      elif w1_val == 'O':
        full[row_num][col_num] = 'O'
      else:
        if w2_val == '.':
          full[row_num][col_num] = w1_val
        else:
          full[row_num][col_num] = 'X'
  return full

def calculate_distance(grid, row_origin, col_origin):
  start_x = row_origin
  start_y = col_origin
  distances = []
  for row_num, row in enumerate(grid):
    for col_num, value in enumerate(row):
      if value == 'X':
        distances.append(abs(row_num-row_origin)+abs(col_num-col_origin))
  return min(distances) if distances else -1

with open('input.txt','r') as file:
  wire_1_path = [move for move in file.readline().strip().split(',')]
  wire_2_path = [move for move in file.readline().strip().split(',')]
max_dims_1 = get_max_dimensions(wire_1_path)
max_dims_2 = get_max_dimensions(wire_2_path)
rows = max(max_dims_1[1],max_dims_2[1]) + abs(min(max_dims_1[0],max_dims_2[0])) + 3
cols = max(max_dims_1[3],max_dims_2[3]) + abs(min(max_dims_1[2],max_dims_2[2])) + 3
row_origin = abs(min(max_dims_1[0], max_dims_2[0]))+1
col_origin = abs(min(max_dims_1[2], max_dims_2[2]))+1

wire_1_grid = generate_grid(rows, cols, row_origin, col_origin)
wire_2_grid = generate_grid(rows, cols, row_origin, col_origin)
full_grid = generate_grid(rows, cols, row_origin, col_origin)
navigate_grid(wire_1_grid, wire_1_path, row_origin, col_origin)
navigate_grid(wire_2_grid, wire_2_path, row_origin, col_origin)
full_grid = generate_full_grid(wire_1_grid, wire_2_grid, full_grid)
distance = calculate_distance(full_grid, row_origin, col_origin)
print('Distance is: ' + str(distance))