
import time
import sys

class Machine:
  name = ''
  data = []
  index = 0
  phase = 0
  inp = 0
  next_machine = None
  take_input = False
  last_output = 0


  def __init__(self, name, data, phase):
    self.name = name
    self.data = data
    self.phase = phase

  def run(self, inp=None):
    global max_value
    # print("running machine", self.name)

    if(inp is not None):
      self.inp = inp

    while True:

      if self.take_input:
        param = inp
      else:
        param = self.phase

      cmd = self.data[self.index]

      i = int(str(cmd)[-2:])
      # print("index:", self.index)
      # print(cmd)
      # print(i)
      # print(self.data)
      # time.sleep(1)
      pointer_inc = 0

      if i == 99:
        # print("machine", self.name, "exited")
        if self.name == "E":
          # print("output value", self.last_output)
          max_value = max(max_value, self.last_output)
          return self.last_output
        return self.next_machine.run()

      a, b = None, None
      if len(str(cmd)) >= 3 and int(str(cmd)[-3:][0]) == 1:
        a = int(self.data[self.index+1])
      else:
        if self.data[self.index+1] < len(self.data):
          a = int(self.data[self.data[self.index+1]])

      if len(str(cmd)) >= 4 and int(str(cmd)[-4:][0]) == 1:
        b = int(self.data[self.index+2])
      else:
        if self.data[self.index+2] < len(self.data):
          b = int(self.data[self.data[self.index+2]])

      if i == 1:
        res = self.data[self.index+3]
        pointer_inc = 4
        self.data[res] = a+b

      elif i == 2:
        res = self.data[self.index+3]
        pointer_inc = 4
        self.data[res] = a*b

      elif i == 3:
        self.take_input = True
        pointer_inc = 2
        self.data[self.data[self.index+1]] = param
        # print("input:", param)

      elif i == 4:
        pointer_inc = 2
        self.index += pointer_inc
        # print("output:", a)
        self.last_output = a
        return self.next_machine.run(a)

      elif i == 5:
        pointer_inc = 3
        if a != 0:
          pointer_inc = 0
          self.index = b

      elif i == 6:
        pointer_inc = 3
        if a == 0:
          pointer_inc = 0
          self.index = b

      elif i == 7:
        pointer_inc = 4
        res = self.data[self.index+3]
        if a < b:
          self.data[res] = 1
        else :
          self.data[res] = 0

      elif i == 8:
        pointer_inc = 4
        res = self.data[self.index+3]
        if a == b:
          self.data[res] = 1
        else :
          self.data[res] = 0 

      else:
        # print("error on machine", self.name, self.data)
        return -1

      # print()
      self.index += pointer_inc

data = [3,26,1001,26,-4,26,3,27,1002,27,2,27,1,27,26,27,4,27,1001,28,-1,28,1005,28,6,99,0,0,5]
# data = [3,15,3,16,1002,16,10,16,1,16,15,15,4,15,99,0,0]
data = [3,52,1001,52,-5,52,3,53,1,52,56,54,1007,54,5,55,1005,55,26,1001,54,-5,54,1105,1,12,1,53,54,53,1008,54,0,55,1001,55,1,55,2,53,55,53,4,53,1001,56,-1,56,1005,56,6,99,0,0,0,0,10]
data = [3,8,1001,8,10,8,105,1,0,0,21,38,63,72,85,110,191,272,353,434,99999,3,9,102,4,9,9,101,2,9,9,102,3,9,9,4,9,99,3,9,1001,9,4,9,102,2,9,9,1001,9,5,9,1002,9,5,9,101,3,9,9,4,9,99,3,9,1001,9,2,9,4,9,99,3,9,1001,9,3,9,102,2,9,9,4,9,99,3,9,101,2,9,9,102,2,9,9,1001,9,2,9,1002,9,4,9,101,2,9,9,4,9,99,3,9,1002,9,2,9,4,9,3,9,102,2,9,9,4,9,3,9,101,2,9,9,4,9,3,9,101,2,9,9,4,9,3,9,101,1,9,9,4,9,3,9,101,2,9,9,4,9,3,9,1002,9,2,9,4,9,3,9,101,2,9,9,4,9,3,9,101,1,9,9,4,9,3,9,1002,9,2,9,4,9,99,3,9,1001,9,1,9,4,9,3,9,102,2,9,9,4,9,3,9,1001,9,2,9,4,9,3,9,102,2,9,9,4,9,3,9,1001,9,2,9,4,9,3,9,101,2,9,9,4,9,3,9,1002,9,2,9,4,9,3,9,1001,9,2,9,4,9,3,9,1001,9,2,9,4,9,3,9,1001,9,1,9,4,9,99,3,9,1001,9,1,9,4,9,3,9,1001,9,1,9,4,9,3,9,1001,9,2,9,4,9,3,9,102,2,9,9,4,9,3,9,1002,9,2,9,4,9,3,9,102,2,9,9,4,9,3,9,1002,9,2,9,4,9,3,9,1002,9,2,9,4,9,3,9,101,2,9,9,4,9,3,9,101,2,9,9,4,9,99,3,9,1001,9,2,9,4,9,3,9,1002,9,2,9,4,9,3,9,101,1,9,9,4,9,3,9,102,2,9,9,4,9,3,9,1001,9,2,9,4,9,3,9,1002,9,2,9,4,9,3,9,102,2,9,9,4,9,3,9,1001,9,2,9,4,9,3,9,1002,9,2,9,4,9,3,9,102,2,9,9,4,9,99,3,9,1002,9,2,9,4,9,3,9,101,1,9,9,4,9,3,9,101,2,9,9,4,9,3,9,101,1,9,9,4,9,3,9,101,2,9,9,4,9,3,9,102,2,9,9,4,9,3,9,101,2,9,9,4,9,3,9,1002,9,2,9,4,9,3,9,1002,9,2,9,4,9,3,9,101,2,9,9,4,9,99]


machines = []

max_value = 0

for p in range(0, 99999+1):
  # print(p)

  done = False
  inp = 0
  p = '%0*d' % (5, p)

  machines = []

  machines.append(Machine('A', data.copy(), int(p[0])))
  machines.append(Machine('B', data.copy(), int(p[1])))
  machines.append(Machine('C', data.copy(), int(p[2])))
  machines.append(Machine('D', data.copy(), int(p[3])))
  machines.append(Machine('E', data.copy(), int(p[4])))

  machines[0].next_machine = machines[1]
  machines[1].next_machine = machines[2]
  machines[2].next_machine = machines[3]
  machines[3].next_machine = machines[4]
  machines[4].next_machine = machines[0]

  if len(p) != len(set([i for i in p])) or int(min(p)) < 5 :
    continue

  machines[0].run(0)

print(max_value)


