"""
Day10
"""
import pprint

input = open("Day10-input.txt",'r').read().split('\n')

X, cycle = 1,1
c_x_list = [[cycle,X]]
CPU = ['.' for _ in range(40*6)]

for line in input:
    if line == "noop":
        cycle += 1
        c_x_list.append([cycle,X])
    else:
        comm, amnt = line.split(' ')
        cycle += 1
        c_x_list.append([cycle,X])
        cycle += 1
        X += int(amnt)
        c_x_list.append([cycle,X])

print(c_x_list)

sum_strength = 0
for i in [20, 60, 100, 140, 180, 220]:
    strength = c_x_list[i-1][0]*c_x_list[i-1][1]
    print(i, strength, c_x_list[i-1][0], c_x_list[i-1][1])
    sum_strength += strength

CPU = ['.' for _ in range(40*6)]

for i in range((40*6)):
    cycle = c_x_list[i][0]
    x = c_x_list[i][1]
    if (cycle-(40*(i//40))) in [x+2, x, x+1]:
        CPU[i] = '#'
        print(cycle, x)


for i in range(0,40*6,40):
    print(''.join(CPU[i:i+40]))