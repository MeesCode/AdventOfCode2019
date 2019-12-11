import math
import time

data = [line.rstrip('\n') for line in open("data.txt")]
pos = []
for y in range(len(data)):
	for x in range(len(data[y])):
		if data[y][x] == '#':
			pos.append((x, y))

# part one
asteroids = []
ms = None
size = 0
for origin in pos:
	comets = []
	phi = []
	dist = []
	for comet in pos:
		if origin == comet: continue
		dx, dy = origin[0]-comet[0], origin[1]-comet[1]
		d = math.atan2(dx, dy)
		d = abs(d) if d <= 0 else 2*math.atan2(0, -1)-d
		comets.append(comet)
		phi.append(d)
		dist.append(math.sqrt(dx*dx+dy*dy))
	if len(set(phi)) > size:
		size = len(set(phi))
		asteroids = [list(i) for i in sorted(sorted(
			zip(phi, comets, dist, [0]*len(phi)), 
			key=lambda x: x[2]),
			key=lambda x: x[0])]
		ms = origin

# part two
i, cd, phi = 0, 0, -1
last = []
while(cd < 450):
	if i >= len(asteroids): i = 0
	c = asteroids[i]
	if c[3] == 0 and c[0] != phi:
		l = list(data[c[1][1]])
		l[c[1][0]] = '.'
		data[c[1][1]] = ''.join(l)
		[print(i) for i in data]
		print()
		time.sleep(0.020)
		c[3] = 1
		phi = c[0]
		cd += 1
		last = c
	i += 1

print("monitoring station", ms, "\nasteroid is sight", size)
print("200th unlucky asteroid", last[1][0]*100+last[1][1])