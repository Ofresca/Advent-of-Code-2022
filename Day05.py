"""
Day 05 of Advent of Code
"""

boxes_start, moves = open("Day05-input.txt",'r').read().split('\n\n')
boxes_start = boxes_start.split('\n')
moves = moves.split('\n')

boxes = [[],[],[],[],[],[],[],[],[]]

for line in boxes_start:
    for i in range(0, len(line), 4):
        if line[i] == '[':
            boxes[i//4].extend([line[i+1]])

# Part 1
for line in moves:
    n_move, from_move, to_move = int(line[5:7]), int(line[12:14])-1, int(line[17:19])-1
    for i in range(0,n_move):
        boxes[to_move].insert(0,boxes[from_move].pop(0))

print(''.join([list[0] for list in boxes]))

# Part 2
for line in moves:
    n_move, from_move, to_move = int(line[5:7]), int(line[12:14])-1, int(line[17:19])-1
    boxes[to_move] = boxes[from_move][:n_move] + boxes[to_move]
    boxes[from_move] = boxes[from_move][n_move:]

print(''.join([list[0] for list in boxes]))


