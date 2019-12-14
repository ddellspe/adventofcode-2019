class Planet:
    def __init__(self, x, y, z):
        self.pos = [x, y, z]
        self.vel = [0, 0, 0]
    def __repr__(self):
        return 'pos=<x=%3d, y=%3d, z=%3d>, vel=<x=%3d, y=%3d, z=%3d>' % (self.pos[0], self.pos[1], self.pos[2], self.vel[0], self.vel[1], self.vel[2])
    def update_velocity(self, planet):
        for i in range(3):
            self.vel[i] += (planet.pos[i] - self.pos[i])/abs(planet.pos[i] - self.pos[i]) if planet.pos[i] != self.pos[i] else 0
    def move_planet(self):
        for i in range(3):
            self.pos[i] += self.vel[i]
    def get_energy(self):
        return sum([abs(val) for val in self.pos])*sum([abs(val) for val in self.vel])


planets = []
with open('input.txt','r') as file:
    for line in file.readlines():
        coords = line.replace('<','').replace('>','')
        [x, y, z] = [int(pos.split('=')[1]) for pos in coords.split(',')]
        planets.append(Planet(x, y, z))
step = 0
step_max = 10
while step < step_max:
    for planet in planets:
        planet.move_planet()
    if step%(step_max//10) == 0:
        print('After', step, 'steps')
        for planet in planets:
            print(planet)
    for planet1 in planets:
        for planet2 in planets:
            if planet1 == planet2:
                continue
            planet1.update_velocity(planet2)
    step += 1
print('After', step, 'steps')
for planet in planets:
    planet.move_planet()
    print(planet)
print('Energy is', sum([planet.get_energy() for planet in planets]))