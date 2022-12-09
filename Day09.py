input = open("Day09-input.txt",'r').read().split('\n')

action = {'R' : [0,1], 'L' : [0,-1], 'U' : [1, 0], 'D' : [-1,0] }

rope = {1: [0,0], 2:[0,0], 3:[0,0], 4:[0,0], 5:[0,0], 6:[0,0], 7:[0,0], 8:[0,0], 9:[0,0], 10:[0,0]}

T_loc = set((0,0))
#Use T_loc.add(y,x)

head, tail = [0,0], [0,0]

for line in input:
    [dir, step] = line.split()
    for i in range(int(step)):
        head_old = head
        head = [head[0] + action[dir][0], head[1] + action[dir][1]]
        if abs(head[0] - tail[0]) > 1 or abs(head[1] - tail[1]) > 1:
            tail = head_old
            T_loc.add((tail[0],tail[1]))

print('Part 1:', len(T_loc))

T_loc = set((0,0))

for line in input:
    [dir, step] = line.split()
    for i in range(int(step)):
        rope[1] = [rope[1][0] + action[dir][0], rope[1][1] + action[dir][1]]
        for idx in range(2,11):
            prev = rope[idx-1]
            next = rope[idx]
            dif_c = prev[0] - next[0]
            dif_r = prev[1] - next[1]
            if abs(dif_c) > 1 or abs(dif_r) > 1:
                if abs(dif_c) >= 1 and abs(dif_r) >= 1:
                    # if not in the same row and not in the same column, move diagonally.
                    if dif_c >= 1:
                        rope[idx][0] = next[0] + 1
                    elif dif_c <= -1:     
                        rope[idx][0] = next[0] - 1
                    if dif_r >= 1:
                        rope[idx][1] = next[1] + 1
                    elif dif_r <= -1:     
                        rope[idx][1] = next[1] - 1                             
                else:
                    if dif_c > 1:
                        rope[idx][0] = next[0] + 1
                    elif dif_c < -1:     
                        rope[idx][0] = next[0] - 1
                    elif dif_r > 1:
                        rope[idx][1] = next[1] + 1
                    elif dif_r < -1:     
                        rope[idx][1] = next[1] - 1 
                if idx == 10:
                    T_loc.add((rope[idx][0],rope[idx][1]))

print('Part 2:', len(T_loc))
    