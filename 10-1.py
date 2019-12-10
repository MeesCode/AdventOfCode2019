
import math

# get data
data = [line.rstrip('\n') for line in open("data10-1.txt")]

# get a list of positions
positions = []
for y in range(len(data)):
	for x in range(len(data[y])):
		if data[y][x] == '#':
			positions.append((y, x))

max_spotted = 0
best_position = (0,0)
for origin in positions:
	spotted = []
	oy, ox = origin
	for comet in positions:
		cy, cx = comet
		if origin == comet:	# if the same; continue
			continue
		elif cy == oy: # if same y axis 
			spotted.append(cx > ox and 90 or 270)
		elif cx == ox:  # if same x axis
			spotted.append(cy > oy and 180 or 0)
		else: # calculate angle
			if cx > ox and cy > oy:	# bottom right
				spotted.append(180-math.degrees(math.atan(abs(cx-ox)/abs(cy-oy))))
			elif cx > ox and cy < oy:	# top right
				spotted.append(math.degrees(math.atan(abs(cx-ox)/abs(cy-oy))))
			elif cx < ox and cy < oy:	# top left
				spotted.append(270+math.degrees(math.atan(abs(cx-ox)/abs(cy-oy))))
			else: # bottom left
				spotted.append(180+math.degrees(math.atan(abs(cx-ox)/abs(cy-oy))))
	if len(set(spotted)) > max_spotted:
		max_spotted = len(set(spotted))
		best_position = origin
print(max_spotted, best_position)