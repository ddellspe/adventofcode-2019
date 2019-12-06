import itertools
from collections import defaultdict

def calculate_path_distance(galaxy, center, running_length):
  if center in galaxy:
    orbit_lengths = 0
    for orbit in galaxy[center]:
      orbit_lengths += calculate_path_distance(galaxy, orbit, running_length+1)
    return running_length + orbit_lengths
  else:
    return running_length

galaxy = defaultdict(list)
with open('input.txt','r') as file:
  for line in file.readlines():
    center, orbit = line.strip().split(')')[0:2]
    galaxy[center].append(orbit)

galaxy = dict(galaxy)
total_path_distance = calculate_path_distance(galaxy, 'COM', 0)
print(total_path_distance)