
import time
import sys

def do(data, index = 0, inp=[]):

    cmd = data[index]

    i = int(str(cmd)[-2:])
    print("index:", index)
    print(cmd)
    # print(i)
    print(data)
    # time.sleep(1)
    pointer_inc = 0

    if i == 99:
        return (data[0], data)

    a, b = None, None
    if len(str(cmd)) >= 3 and int(str(cmd)[-3:][0]) == 1:
        a = data[index+1]
    else:
        if data[index+1] < len(data):
            a = data[data[index+1]]

    if len(str(cmd)) >= 4 and int(str(cmd)[-4:][0]) == 1:
        b = data[index+2]
    else:
        if data[index+2] < len(data):
            b = data[data[index+2]]

    if i == 1:
        res = data[index+3]
        pointer_inc = 4
        data[res] = a+b

    elif i == 2:
        res = data[index+3]
        pointer_inc = 4
        data[res] = a*b

    elif i == 3:
        pointer_inc = 2
        data[data[index+1]] = inp.pop(0)

    elif i == 4:
        pointer_inc = 2
        # print("output:", a)
        return (data[0], data, a)

    elif i == 5:
        pointer_inc = 3
        if a != 0:
            pointer_inc = 0
            index = b

    elif i == 6:
        pointer_inc = 3
        if a == 0:
            pointer_inc = 0
            index = b

    elif i == 7:
        pointer_inc = 4
        res = data[index+3]
        if a < b:
            data[res] = 1
        else :
            data[res] = 0

    elif i == 8:
        pointer_inc = 4
        res = data[index+3]
        if a == b:
            data[res] = 1
        else :
            data[res] = 0 

    else:
        # print("error!", data)
        return 

    (result, l, inp) = do(data, index+pointer_inc, inp)
    return (result, l, inp)

data = [3,8,1001,8,10,8,105,1,0,0,21,38,63,72,85,110,191,272,353,434,99999,3,9,102,4,9,9,101,2,9,9,102,3,9,9,4,9,99,3,9,1001,9,4,9,102,2,9,9,1001,9,5,9,1002,9,5,9,101,3,9,9,4,9,99,3,9,1001,9,2,9,4,9,99,3,9,1001,9,3,9,102,2,9,9,4,9,99,3,9,101,2,9,9,102,2,9,9,1001,9,2,9,1002,9,4,9,101,2,9,9,4,9,99,3,9,1002,9,2,9,4,9,3,9,102,2,9,9,4,9,3,9,101,2,9,9,4,9,3,9,101,2,9,9,4,9,3,9,101,1,9,9,4,9,3,9,101,2,9,9,4,9,3,9,1002,9,2,9,4,9,3,9,101,2,9,9,4,9,3,9,101,1,9,9,4,9,3,9,1002,9,2,9,4,9,99,3,9,1001,9,1,9,4,9,3,9,102,2,9,9,4,9,3,9,1001,9,2,9,4,9,3,9,102,2,9,9,4,9,3,9,1001,9,2,9,4,9,3,9,101,2,9,9,4,9,3,9,1002,9,2,9,4,9,3,9,1001,9,2,9,4,9,3,9,1001,9,2,9,4,9,3,9,1001,9,1,9,4,9,99,3,9,1001,9,1,9,4,9,3,9,1001,9,1,9,4,9,3,9,1001,9,2,9,4,9,3,9,102,2,9,9,4,9,3,9,1002,9,2,9,4,9,3,9,102,2,9,9,4,9,3,9,1002,9,2,9,4,9,3,9,1002,9,2,9,4,9,3,9,101,2,9,9,4,9,3,9,101,2,9,9,4,9,99,3,9,1001,9,2,9,4,9,3,9,1002,9,2,9,4,9,3,9,101,1,9,9,4,9,3,9,102,2,9,9,4,9,3,9,1001,9,2,9,4,9,3,9,1002,9,2,9,4,9,3,9,102,2,9,9,4,9,3,9,1001,9,2,9,4,9,3,9,1002,9,2,9,4,9,3,9,102,2,9,9,4,9,99,3,9,1002,9,2,9,4,9,3,9,101,1,9,9,4,9,3,9,101,2,9,9,4,9,3,9,101,1,9,9,4,9,3,9,101,2,9,9,4,9,3,9,102,2,9,9,4,9,3,9,101,2,9,9,4,9,3,9,1002,9,2,9,4,9,3,9,1002,9,2,9,4,9,3,9,101,2,9,9,4,9,99]
# data = [3,23,3,24,1002,24,10,24,1002,23,-1,23,101,5,23,23,1,24,23,23,4,23,99,0,0]
data = [3,15,3,16,1002,16,10,16,1,16,15,15,4,15,99,0,0]
# data = [3,31,3,32,1002,32,10,32,1001,31,-2,31,1007,31,0,33,1002,33,7,33,1,33,31,31,1,32,31,31,4,31,99,0,0,0]
max_inp = 0
max_phase = ''

for p in range(0, 44444+1):

    inp = 0
    p = '%0*d' % (5, p)

    if len(str(p)) != len(set([i for i in str(p)])) or int(max(str(p))) > 4 :
        continue

    for c in p:
        (_, data, inp) = do(data, inp=[int(c), inp])
    if inp > max_inp:
        # print(p, inp)
        max_inp = inp
        max_phase = p

print("output:", max_inp)
