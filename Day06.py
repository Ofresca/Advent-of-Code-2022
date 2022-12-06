"""
Day 06 of Advent of Code
"""

input = open("Day06-input.txt",'r').read()

len_str = 4

for i in range(len_str,len(input)):
    test_string = input[(i-len_str):i]
    if len(set(test_string)) == len_str:
        result = i
        break

print('Part 1:', result)

len_str = 14

for i in range(len_str,len(input)):
    test_string = input[(i-len_str):i]
    if len(set(test_string)) == len_str:
        result = i
        break

print('Part 2:', result)
