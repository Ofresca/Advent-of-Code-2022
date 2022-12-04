"""
Day 04 of Advent of Code
"""

import re

input = open("Day04-input.txt",'r').read().split('\n')

counter = 0
for line in input:
    min1, max1, min2, max2 = map(int, re.split(',|-',line))
    if (min1 <= min2 and max1 >= max2) or (min1 >= min2 and max1 <= max2):
        counter += 1
    
print('Part 1:', counter)

counter = 0
for line in input:
    min1, max1, min2, max2 = map(int, re.split(',|-',line))
    if not (min1 > max2 or min2 > max1):
        counter += 1

print('Part 2:', counter)
