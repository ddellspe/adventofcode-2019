from functools import reduce
import math

class Planet:
    def __init__(self, x=0, y=0, z=0, planet=None):
        if planet:
            self.pos = planet.pos.copy()
            self.vel = planet.vel.copy()
        else:
            self.pos = [x, y, z]
            self.vel = [0, 0, 0]
    def __repr__(self):
        return 'pos=<x=%3d, y=%3d, z=%3d>, vel=<x=%3d, y=%3d, z=%3d>' % (self.pos[0], self.pos[1], self.pos[2], self.vel[0], self.vel[1], self.vel[2])

    def __eq__(self, obj):
        return isinstance(obj, Planet) and self.pos == obj.pos and self.vel == obj.vel
    def update_velocity(self, planet):
        for i in range(3):
            self.vel[i] += (planet.pos[i] - self.pos[i])/abs(planet.pos[i] - self.pos[i]) if planet.pos[i] != self.pos[i] else 0
    def move_planet(self):
        for i in range(3):
            self.pos[i] += self.vel[i]
    def get_energy(self):
        return sum([abs(val) for val in self.pos])*sum([abs(val) for val in self.vel])

def lcm(a, b):
    return (a * b) // math.gcd(a, b)
planets = []
with open('input.txt','r') as file:
    for line in file.readlines():
        coords = line.replace('<','').replace('>','')
        [x, y, z] = [int(pos.split('=')[1]) for pos in coords.split(',')]
        planets.append(Planet(x, y, z))
step = 0
period = dict()
start = [[(p.pos[axis], p.vel[axis]) for p in planets] for axis in range(3)]
while len(period) < 3:
    step+=1
    for planet1 in planets:
        for planet2 in planets:
            if planet1 == planet2:
                continue
            planet1.update_velocity(planet2)
    for planet in planets:
        planet.move_planet()
    for axis in range(3):
        if axis not in period and start[axis] == [(p.pos[axis], p.vel[axis]) for p in planets]:
            period[axis] = step
print(start, period)
print('After', step, 'steps')
print('ans:', reduce(lcm, period.values()))