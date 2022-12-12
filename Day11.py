import re
from pprint import pprint

input = open("Day11-input.txt",'r').read().split('\n\n')

class Monkey:

    def __init__(self, operation, test, if_true, if_false, items = []):
        self.items = items
        self.operation = operation
        self.test = int(test)
        self.if_true = if_true
        self.if_false = if_false
        self.inspect = 0
    
    def process_items(self, apes, divisor):
        for item in self.items:
            old = item
            item = eval(self.operation)
            item %= divisor
            if item % self.test == 0:
                new_monkey = int(self.if_true)
            else:
                new_monkey = int(self.if_false)
            apes[new_monkey].items.append(item)
            self.inspect += 1
        self.items = []
    
apes = []
divisor = 1

for line in input:
    properties = line.split('\n')
    monkey = properties[0].replace(":", "").replace(' ', '').lower()
    items = [int(i) for i in re.findall('\d+', properties[1])]
    operation = properties[2].split('= ')[1]
    test = int(properties[3].split()[-1])
    if_true = properties[4].split()[-1]
    if_false = properties[5].split()[-1]

    monkey = Monkey(operation, test, if_true, if_false, items)
    divisor *= test
    apes.append(monkey)

for _ in range(10000):
    for ape in apes:
        ape.process_items(apes, divisor)

activity = []
for ape in apes:
    activity.append(ape.inspect)

activity.sort()
print(activity[-1]*activity[-2])



    






