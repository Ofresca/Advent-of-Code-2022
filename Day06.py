"""
Day 06 of Advent of Code
"""

input = open("Day06-input.txt",'r').read()

len_str = 4
for i in range(len_str,len(input)):
    if len(set(input[(i-len_str):i])) == len_str:
        break

print('Part 1:', i)

len_str = 14
for i in range(len_str,len(input)):
    if len(set(input[(i-len_str):i])) == len_str:
        break

print('Part 2:', i)
