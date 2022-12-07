"""
Day 06 of Advent of Code
"""

input = open("Day06-input.txt",'r').read()

def find_string(n):
    for i in range(n,len(input)):
        if len(set(input[(i-n):i])) == n:
            return i

print('Part 1:', find_string(4))
print('Part 2:', find_string(14))