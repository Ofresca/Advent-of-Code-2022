"""
Day 05 of Advent of Code
"""
from copy import deepcopy

boxes_start, moves = open("Day05-input.txt",'r').read().split('\n\n')
boxes_start = boxes_start.split('\n')
moves = moves.split('\n')

boxes_1 = [[] for _ in range(9)]

for line in boxes_start:
    for i in range(0, len(line), 4):
        if line[i] == '[':
            boxes_1[i//4].append(line[i+1])

boxes_2 = deepcopy(boxes_1)

# Part 1
for line in moves:
    n_move, from_move, to_move = int(line[5:7]), int(line[12:14])-1, int(line[17:19])-1
    for _ in range(0,n_move):
        boxes_1[to_move].insert(0,boxes_1[from_move].pop(0))

print(''.join([list[0] for list in boxes_1]))

# Part 2
for line in moves:
    n_move, from_move, to_move = int(line[5:7]), int(line[12:14])-1, int(line[17:19])-1
    boxes_2[to_move] = boxes_2[from_move][:n_move] + boxes_2[to_move]
    boxes_2[from_move] = boxes_2[from_move][n_move:]

print(''.join([list[0] for list in boxes_2]))


