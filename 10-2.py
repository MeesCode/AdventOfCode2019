
import math

# get data
data = [line.rstrip('\n') for line in open("data10-1.txt")]

# get a list of positions
positions = []
for y in range(len(data)):
	for x in range(len(data[y])):
		if data[y][x] == '#':
			positions.append((x, y))

max_spotted = 0
best_position = (0,0)
degrees_comet = []
list_comet = []
for origin in positions:
# origin = (0,0)
	spotted = []
	degrees = []
	ox, oy = origin
	for comet in positions:
		cx, cy = comet
		if origin == comet:	# if the same; continue
			continue
		elif cy == oy: # if same y axis 
			d = cx > ox and 90 or 270
		elif cx == ox:  # if same x axis
			d = cy > oy and 180 or 0
		else: # calculate angle
			if cx > ox and cy > oy:	# bottom right
				d = 180-math.degrees(math.atan(abs(cx-ox)/abs(cy-oy)))
			elif cx > ox and cy < oy:	# top right
				d = math.degrees(math.atan(abs(cx-ox)/abs(cy-oy)))
			elif cx < ox and cy < oy:	# top left
				d = 360-math.degrees(math.atan(abs(cx-ox)/abs(cy-oy)))
			else: # bottom left
				d = 180+math.degrees(math.atan(abs(cx-ox)/abs(cy-oy)))
		spotted.append(comet)
		degrees.append(d)
	if len(set(degrees)) > max_spotted:
		list_comet = spotted
		max_spotted = len(set(degrees))
		degrees_comet = degrees
		best_position = origin

# print("best position", best_position)

# we now know the best position, create
# and ordered list of comets to be destroyed
def getDegrees(item):
	return item[0]

def getDistance(item):
	return item[2]

distances = [math.sqrt(math.pow(best_position[0] - i[0], 2) + math.pow(best_position[1] - i[1], 2)) for i in list_comet]
# print(distances)
destroyed = [0] * len(list_comet)
comet_list = sorted(sorted(zip(degrees_comet, list_comet, distances, destroyed), key=getDistance), key=getDegrees)
comet_list = [list(i) for i in comet_list]

destroyed_degrees = []
destroyed_counter = 0
index = 0
last_destroyed = []
while(destroyed_counter < 200):
	if index >= len(comet_list):
		index = 0
		destroyed_degrees = []
		# print("swoop")
	c = comet_list[index]
	if c[3] == 0 and c[0] not in destroyed_degrees:
		c[3] = 1
		destroyed_degrees.append(c[0])
		destroyed_counter += 1
		last_destroyed = c
		# print("destroyed:", destroyed_counter, c[1])
	index += 1

print(last_destroyed[1][0]*100+last_destroyed[1][1])
# [print(i) for i in comet_list]