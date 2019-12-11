class Machine:
  index, relative_base = 0, 0
  index_inc = [4, 4, 2, 2, 3, 3, 4, 4, 2]
  data = []

  def __init__(self, data):
    self.data = data

  def parse_instruction(self, cmd):
    cmd = '%0*d' % (5, cmd)
    p = []
    for i, c in enumerate(cmd[:3][::-1]):
      if c == '0': pointer = self.data[self.index+i+1]
      elif c == '1': pointer = self.index+i+1
      else: pointer = self.relative_base+self.data[self.index+i+1]
      if c in ['1', '2'] and len(data) <= pointer: data.extend([0] * (pointer-len(data)+1))
      p.append(pointer)
    return int(cmd[-2:]), p
    
  def run(self):
    while True:
      opcode, p = self.parse_instruction(self.data[self.index])
      if opcode == 99: return 
      self.index += self.index_inc[opcode-1]
      if opcode == 1: self.data[p[2]] = self.data[p[0]]+self.data[p[1]]
      elif opcode == 2: self.data[p[2]] = self.data[p[0]]*self.data[p[1]]
      elif opcode == 3: self.data[p[0]] = int(input('input: '))
      elif opcode == 4: print('output:', self.data[p[0]])
      elif opcode == 5 and self.data[p[0]] != 0: self.index = self.data[p[1]]
      elif opcode == 6 and self.data[p[0]] == 0: self.index = self.data[p[1]]
      elif opcode == 7: self.data[p[2]] = self.data[p[0]] < self.data[p[1]] and 1 or 0
      elif opcode == 8: self.data[p[2]] = self.data[p[0]] == self.data[p[1]] and 1 or 0
      elif opcode == 9: self.relative_base += self.data[p[0]]

data = [int(i) for i in [line.split(',') for line in open('data.txt')][0]]
Machine(data).run()

