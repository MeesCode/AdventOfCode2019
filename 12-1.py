from functools import reduce

data = [line.rstrip('\n') for line in open("data.txt")]
data = [i[1:len(i)-1].split(',') for i in data]
data = [[int(i.split('=')[1]) for i in j] for j in data]

# print(data)

class Moon:
    vx, vy, vz = 0, 0, 0
    px, py, pz = 0, 0, 0
    def __init__(self, x, y, z):
        self.x = x
        self.y = y
        self.z = z
        self.ox = x
        self.oy = y
        self.oz = z

    def periodsFound(self):
        return 0 not in [self.px, self.py, self.pz]

    def pot(self):
        return abs(self.x) + abs(self.y) + abs(self.z)

    def kin(self):
        return abs(self.vx) + abs(self.vy) + abs(self.vz)

    def __str__(self):
        return str(self.x) + ',' + str(self.y) + ',' + str(self.z) + ' - ' + str(self.vx) + ',' + str(self.vy) + ',' + str(self.vz) + ' - ' + str(self.px) + ',' + str(self.py) + ',' + str(self.pz) + ';'

moons = [Moon(p[0], p[1], p[2]) for p in data]

def printMoons(moons):
    for i in moons:
        print(i)
    print()

def allPeriodsFound(moons):
    for i in moons:
        if not i.periodsFound(): return False
    return True

def lcm(a, b):
    if a > b:
        greater = a
    else:
        greater = b

    while True:
        if greater % a == 0 and greater % b == 0:
            lcm = greater
            break
        greater += 1

    return lcm

def get_lcm_for(your_list):
    return reduce(lambda x, y: lcm(x, y), your_list)

periodx, periody, periodz = 0,0,0

for c in range(9999999999999999):
    for (x, y) in [(0, 1), (0, 2), (0, 3), (1, 2), (1, 3), (2, 3)]:
        a = moons[x]
        b = moons[y]
        if a == b: continue
        if a.x > b.x: 
            a.vx -= 1
            b.vx += 1
        elif a.x < b.x: 
            a.vx += 1
            b.vx -= 1

        if a.y > b.y: 
            a.vy -= 1
            b.vy += 1
        elif a.y < b.y: 
            a.vy += 1
            b.vy -= 1

        if a.z > b.z: 
            a.vz -= 1
            b.vz += 1
        elif a.z < b.z: 
            a.vz += 1
            b.vz -= 1

    for i in moons:
        i.x += i.vx
        i.y += i.vy
        i.z += i.vz

    if periodx == 0 and moons[0].x == moons[0].ox and moons[1].x == moons[1].ox and moons[2].x == moons[2].ox and moons[3].x == moons[3].ox : periodx = c + 2
    if periody == 0 and moons[0].y == moons[0].oy and moons[1].y == moons[1].oy and moons[2].y == moons[2].oy and moons[3].y == moons[3].oy : periody = c + 2
    if periodz == 0 and moons[0].z == moons[0].oz and moons[1].z == moons[1].oz and moons[2].z == moons[2].oz and moons[3].z == moons[3].oz : periodz = c + 2

    if 0 not in [periodx, periody, periodz]:
        break

printMoons(moons)
l = [periodx, periody, periodz]

print(l)

print(get_lcm_for(l))

# result = 0
# for i in moons:
#     result += i.pot() * i.kin()
# print("energy", result)
