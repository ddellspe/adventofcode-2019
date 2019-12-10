import itertools
import math
from collections import defaultdict

with open('input.txt', 'r') as file:
    map = [[element for element in line.strip()] for line in file.readlines()]

asteroid_list = []
for row_num, row in enumerate(map):
    for col_num, value in enumerate(row):
        if value == '#':
            asteroid_list.append((row_num, col_num))
unobstructed_asteroid_count = defaultdict(lambda: 0)
degrees = defaultdict(lambda: defaultdict(lambda: float))
distances = defaultdict(lambda: defaultdict(lambda: float))
for asteroid in asteroid_list:
    for target in asteroid_list:
        if target == asteroid:
            continue
        degrees[asteroid][target] = math.fmod(
            math.degrees(math.atan2(target[0] - asteroid[0], target[1] - asteroid[1])) + 450.0, 360.0)
        distances[asteroid][target] = math.sqrt(
            math.pow(abs(asteroid[0] - target[0]), 2) + math.pow(abs(asteroid[1] - target[1]), 2))
        if asteroid[0] == target[0]:
            row_num = asteroid[0]
            direction = 1 if asteroid[1] < target[1] else -1
            blocked = False
            for col_num in range(asteroid[1] + direction, target[1], direction):
                if map[row_num][col_num] == '#':
                    blocked = True
                    break
            if not blocked:
                unobstructed_asteroid_count[asteroid] += 1
        elif asteroid[1] == target[1]:
            col_num = asteroid[1]
            direction = 1 if asteroid[0] < target[0] else -1
            blocked = False
            for row_num in range(asteroid[0] + direction, target[0], direction):
                if map[row_num][col_num] == '#':
                    blocked = True
                    break
            if not blocked:
                unobstructed_asteroid_count[asteroid] += 1
        else:
            direction = 1 if asteroid[0] < target[0] else -1
            col_diff = abs(asteroid[1] - target[1]) * (1 if asteroid[1] < target[1] else -1)
            row_diff = abs(asteroid[0] - target[0]) * direction
            slope = col_diff / row_diff
            blocked = False
            for row_num in range(asteroid[0] + direction, target[0], direction):
                col_num = asteroid[1] + (row_num - asteroid[0]) * slope
                if col_num == col_num // 1 and map[row_num][int(col_num // 1)] == '#':
                    blocked = True
                    break
            if not blocked:
                unobstructed_asteroid_count[asteroid] += 1
        degrees[asteroid] = dict(degrees[asteroid])
max_asteroid, max_count = list(unobstructed_asteroid_count.items())[0]
for asteroid, count in unobstructed_asteroid_count.items():
    if count > max_count:
        max_asteroid = asteroid
        max_count = count
print((max_asteroid[1], max_asteroid[0]), max_count)
asteroids_by_slope = defaultdict(list)
for asteroid, slope in degrees[max_asteroid].items():
    asteroids_by_slope[slope].append((asteroid, distances[max_asteroid][asteroid]))
values = list(itertools.chain.from_iterable(list(asteroids_by_slope.values())))
destroyed = []
while len(values) - len(destroyed) > 0:
    for slope in sorted(list(asteroids_by_slope.keys())):
        for asteroid_bundle in sorted(asteroids_by_slope[slope], key=lambda x: x[1]):
            if asteroid_bundle in destroyed:
                continue
            destroyed.append(asteroid_bundle)
            break
print(destroyed[199][0][1]*100+destroyed[199][0][0])