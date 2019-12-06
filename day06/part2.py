import itertools
from collections import defaultdict

path_distances = {}
path_lists = defaultdict(list)

def calculate_path_distance(galaxy, center, running_length):
  if center in galaxy:
    orbit_lengths = 0
    for orbit in galaxy[center]:
      path_lists[orbit] = path_lists[center].copy()
      path_lists[orbit].append(center)
      orbit_lengths += calculate_path_distance(galaxy, orbit, running_length+1)
    path_distances[center] = running_length
    return running_length + orbit_lengths
  else:
    path_distances[center] = running_length
    return running_length

def get_common_points(entity_one, entity_two, paths):
  common_points = []
  for point in paths[entity_one]:
    if point in paths[entity_two]:
      common_points.append(point)
  return common_points

def get_max_common_point(points, distances):
  point = points[0]
  for pt in points:
    if distances[pt] > distances[point]:
      point = pt
  return point

galaxy = defaultdict(list)
with open('input.txt','r') as file:
  for line in file.readlines():
    center, orbit = line.strip().split(')')[0:2]
    galaxy[center].append(orbit)

galaxy = dict(galaxy)
total_path_distance = calculate_path_distance(galaxy, 'COM', 0)
common_points = get_common_points('YOU', 'SAN', path_lists)
common_point = get_max_common_point(common_points, path_distances)
print(path_distances['YOU'] + path_distances['SAN'] - (2 * (path_distances[common_point] + 1)))