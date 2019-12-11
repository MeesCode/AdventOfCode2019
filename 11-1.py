class Machine:
	index, relative_base = 0, 0
	index_inc = [4, 4, 2, 2, 3, 3, 4, 4, 2]
	data = []
	output = []

	def __init__(self, data):
		self.data = data

	def parse_instruction(self, cmd):
		cmd, p = ('%0*d' % (5, cmd)), []
		for i, c in enumerate(cmd[:3][::-1]):
			if c == '0': pointer = self.data[self.index+i+1]
			elif c == '1': pointer = self.index+i+1
			else: pointer = self.relative_base+self.data[self.index+i+1]
			# if len(data) < pointer: data.extend([0] * (pointer-len(data)+1))
			p.append(pointer)
		return int(cmd[-2:]), p
	
	def run(self):
		global x, y
		while True:
			opcode, p = self.parse_instruction(self.data[self.index])
			if opcode == 99: return self.output
			self.index += self.index_inc[opcode-1]
			if opcode == 1: self.data[p[2]] = self.data[p[0]]+self.data[p[1]]
			elif opcode == 2: self.data[p[2]] = self.data[p[0]]*self.data[p[1]]
			elif opcode == 3: 
				self.data[p[0]] = getTileAtPosition((x, y)).color
			elif opcode == 4: 
				self.output.append(self.data[p[0]])
				if len(self.output) == 2:
					getTileAtPosition((x, y)).paint(self.output[0])
					changeCord(self.output[1])
					self.output = []
			elif opcode == 5 and self.data[p[0]] != 0: self.index = self.data[p[1]]
			elif opcode == 6 and self.data[p[0]] == 0: self.index = self.data[p[1]]
			elif opcode == 7: self.data[p[2]] = self.data[p[0]] < self.data[p[1]] and 1 or 0
			elif opcode == 8: self.data[p[2]] = self.data[p[0]] == self.data[p[1]] and 1 or 0
			elif opcode == 9: self.relative_base += self.data[p[0]]

class Tile:
	color = 0
	cord = (0, 0)
	painted = False

	def __init__(self, cord, color=0):
		self.cord = cord
		self.color = color

	def paint(self, color):
		if color != self.color:
			self.color = color
			self.painted = True

direction = 0
x, y = 0, 0
tiles = [Tile((0, 0), 1)]

def getTileAtPosition(cord):
	global tiles
	for t in tiles:
		if cord == t.cord:
			return t
	t = Tile(cord)
	tiles.append(t)
	return t

def changeCord(i):
	global x, y, direction
	if i == 0: direction -= 1
	else: direction += 1

	if direction == 4: direction = 0
	if direction == -1: direction = 3

	if direction == 0: y += 1
	elif direction == 1: x += 1
	if direction == 2: y -= 1
	elif direction == 3: x -= 1

data = [int(i) for i in [line.split(',') for line in open('data.txt')][0]]
data.extend([0]*10000)
Machine(data).run()

minx, miny, maxx, maxy = 0, 0, 0, 0

for i in tiles:
	minx = min(i.cord[0], minx)
	maxx = max(i.cord[0], maxx)
	miny = min(i.cord[1]-2, miny)
	maxy = max(i.cord[1], maxy)
	i.cord = list(i.cord)

w, h = maxx - minx, maxy - miny

for i in tiles:
	i.cord[0] = i.cord[0] - minx
	i.cord[1] = i.cord[1] - minx

pic = []
for i in range(h):
	pic.append([' ']*w)

for i in tiles:
	if i.color == 1:
		pic[i.cord[1]][i.cord[0]] = '#'

for i in pic[::-1]:
	print("".join(i))

