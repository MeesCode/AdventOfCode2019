
data = [line.rstrip('\n') for line in open("data.txt")]

class Element():
    create = []
    amount = 0
    needed = 0

    def __init__(self, name):
        self.name = name

    def __str__(self):
        string = self.name + ' ['
        for i in self.create:
            string += '(' + i[0].name + ', ' + str(i[1]) + '), '
        string = string[:len(string)-2] + '] needed: ' + str(self.needed)
        return string

    def __eq__(self, other):
        return self.name == other.name

    def __neq__(self, other):
        return self.name != other.name

    def __hash__(self):
        return hash(self.name)

def getElement(name):
    global elements
    for i in elements:
        if i.name == name: return i
    e = Element(name)
    elements.append(e)
    return e

# a: number to multiply
# b: number to compare with
# return: amount of multiplications needed
def mulUntilHihgher(a, b):
    mul = 1
    while a*mul < b:
        mul += 1
    return a*mul


# create a list of all elements
elements = []
for i in data:
    i = i.split('=>')
    react, el = i[0], i[1][1:]
    a, n = el.split(' ')[0], el.split(' ')[1]
    el = getElement(n)
    el.amount = int(a)

    reactions = []
    for r in react.split(','):
        if r[0] == ' ': r = r[1:]
        a, n = r.split(' ')[0], r.split(' ')[1]
        rel = getElement(n)
        reactions.append((rel, int(a)))
    
    el.create = reactions

el = getElement('FUEL')
level = [el]
el.needed = 1
while len(level) > 0:
    [print(str(e)) for e in level]
    element = level.pop(0)
    for i in element.create:
        if(i[0] not in level): level.append(i[0])
        name, amount = i
        reactor = i[0]
        mul = mulUntilHihgher(element.amount, element.needed)
        print("mul", mul//element.amount)
        a = i[1] * (mul//element.amount)
        reactor.needed += a
        print("added", a, "to", reactor.name)

    print()

print("elements")
[print(str(e)) for e in elements]

# get elements that can directly convert ore
el = []
for i in elements:
    if i.name == 'ORE': continue
    if i.create[0][0].name == "ORE":
        el.append(i)

ore = getElement('ORE')
ore.needed = 0

for i in el:
    mul = mulUntilHihgher(i.amount, i.needed)
    print("mul", mul//i.amount)
    a = i.create[0][1] * (mul//i.amount)
    reactor.needed += a
    print("added", a, "to", reactor.name)

print(str(ore))