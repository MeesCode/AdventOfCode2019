import numpy as np
import itertools

class Moon:
    vx, vy, vz = 0, 0, 0
    def __init__(self, x, y, z):
        self.x, self.ox = x, x
        self.y, self.oy = y, y
        self.z, self.oz = z, z

    def energy(self):
        return sum([abs(i) for i in [self.x + self.y + self.z]]) * sum([abs(i) for i in [self.vx + self.vy + self.vz]])

m = [Moon(p[0], p[1], p[2]) for p in 
[[int(i.split('=')[1]) for i in j] for j in 
[i[1:len(i)-1].split(',') for i in 
[line.rstrip('\n') for line in 
open("data.txt")]]]]

px, py, pz = 0,0,0
for c in itertools.count():
    for (x, y) in [(0, 1), (0, 2), (0, 3), (1, 2), (1, 3), (2, 3)]:
        a, b = m[x], m[y]
        if a == b: continue
        if a.x > b.x: a.vx, b.vx = a.vx-1, b.vx+1
        elif a.x < b.x: a.vx, b.vx = a.vx+1, b.vx-1
        if a.y > b.y: a.vy, b.vy = a.vy-1, b.vy+1
        elif a.y < b.y: a.vy, b.vy = a.vy+1, b.vy-1
        if a.z > b.z: a.vz, b.vz = a.vz-1, b.vz+1
        elif a.z < b.z: a.vz, b.vz = a.vz+1, b.vz-1

    for i in m:
        i.x += i.vx
        i.y += i.vy
        i.z += i.vz

    if px == 0 and m[0].x == m[0].ox and m[1].x == m[1].ox and m[2].x == m[2].ox and m[3].x == m[3].ox : px = c + 2
    if py == 0 and m[0].y == m[0].oy and m[1].y == m[1].oy and m[2].y == m[2].oy and m[3].y == m[3].oy : py = c + 2
    if pz == 0 and m[0].z == m[0].oz and m[1].z == m[1].oz and m[2].z == m[2].oz and m[3].z == m[3].oz : pz = c + 2
    if 0 not in [px, py, pz]: break

print("energy", sum([i.energy() for i in m])) # part 1
print("period", np.lcm.reduce([px, py, pz])) # part 2
