from collections import defaultdict

with open('input.txt','r') as file:
    map = [[element for element in line.strip()] for line in file.readlines()]

asteroid_list = []
for row_num, row in enumerate(map):
    for col_num, value in enumerate(row):
        if value == '#':
            asteroid_list.append((row_num,col_num))
unobstructed_asteroid_count = defaultdict(lambda: 0)
for asteroid in asteroid_list:
    for target in asteroid_list:
        if target == asteroid:
            continue
        if asteroid[0] == target[0]:
            row_num = asteroid[0]
            direction = 1 if asteroid[1] < target[1] else -1
            blocked = False
            for col_num in range(asteroid[1]+direction, target[1], direction):
                if map[row_num][col_num] == '#':
                    blocked = True
                    break
            if not blocked:
                unobstructed_asteroid_count[asteroid] += 1
        elif asteroid[1] == target[1]:
            col_num = asteroid[1]
            direction = 1 if asteroid[0] < target[0] else -1
            blocked = False
            for row_num in range(asteroid[0]+direction, target[0], direction):
                if map[row_num][col_num] == '#':
                    blocked = True
                    break
            if not blocked:
                unobstructed_asteroid_count[asteroid] += 1
        else:
            direction = 1 if asteroid[0] < target[0] else -1
            col_diff = abs(asteroid[1] - target[1])*(1 if asteroid[1] < target[1] else -1)
            row_diff = abs(asteroid[0] - target[0])*direction
            slope = col_diff/row_diff
            #print('\t\t', row_diff, col_diff, slope)
            blocked = False
            for row_num in range(asteroid[0]+direction, target[0], direction):
                col_num = asteroid[1] + (row_num-asteroid[0])*slope
                if col_num == col_num//1 and map[row_num][int(col_num//1)] == '#':
                    blocked = True
                    break
            if not blocked:
                unobstructed_asteroid_count[asteroid] += 1

max_asteroid, max_count = list(unobstructed_asteroid_count.items())[0]
for asteroid, count in unobstructed_asteroid_count.items():
    if count > max_count:
        max_asteroid = asteroid
        max_count = count
print((max_asteroid[1], max_asteroid[0]), max_count)