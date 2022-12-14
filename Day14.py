import string
import pprint

input = open("Day14-input.txt",'r').read().split('\n')

values = []
xy_coord = []
for line in input:
    values.append([x for x in line.split(' -> ')])
for line in values:
        xy_coord.append([[int(x) for x in item.split(',')]for item in line])

# print(xy_coord)

max_x, max_y = 0, 0
min_x, min_y = xy_coord[0][0]
#Find min and max values of x and y values.
for list in xy_coord:
    for [x,y] in list:
        if x > max_x: max_x = x
        if y > max_y: max_y = y
        if x < min_x: min_x = x
        if y < min_y: min_y = y

print('min_x', min_x,'min_y', min_y)
print('max_x', max_x,'max_y', max_y)
print('dif_x', max_x - min_x, 'dif_y', max_y-min_y)

#Create grid of size (max_x - min_x) * (max_y - min_y)
# grid = [['.' for _ in range(max_x-min_x+2)] for _ in range(max_y+1)]

# # pprint.pprint(grid)  

# #Fill the grid with the values from xy_coord
# #Xcoord = value - min_x + 1
# #Ycoord = value - min_y + 1
# for line in xy_coord:
#     for i in range(len(line)-1):
#         [f_x, f_y] = line[i]
#         [t_x, t_y] = line[i+1]
#         [f_x, f_y] = [f_x - min_x + 1, f_y]
#         [t_x, t_y] = [t_x - min_x + 1, t_y]
#         if f_x == t_x and f_y != t_y:
#             k = f_x
#             for l in range(min(f_y, t_y), max(f_y, t_y)+1,1):
#                 grid[l][k] = '#'
#         elif f_x != t_x and f_y == t_y:
#             l = f_y
#             for k in range(min(f_x, t_x), max(f_x, t_x)+1,1):
#                 grid[l][k] = '#'
#         else:
#             for k in range(min(f_x, t_x), max(f_x, t_x)+1,1):
#                 for l in range(min(f_y, t_y), max(f_y, t_y)+1,1):
#                     grid[l][k] = '#'  

# # pprint.pprint(grid)  
# changed to max_y + 3 from + 1
# changed to max_x from max_x-min_x+2
grid = [['.' for _ in range((max_y+3)*2)] for _ in range(max_y+3)]

# all x positions should be + 1/2 y
half_y = int((max_y+3)//2)
# pprint.pprint(grid)  

#Fill the grid with the values from xy_coord
#Xcoord = value - min_x + 1
#Ycoord = value - min_y + 1
for line in xy_coord:
    for i in range(len(line)-1):
        [f_x, f_y] = line[i]
        [t_x, t_y] = line[i+1]
        [f_x, f_y] = [f_x - min_x + half_y, f_y]
        [t_x, t_y] = [t_x - min_x + half_y, t_y]
        if f_x == t_x and f_y != t_y:
            k = f_x
            for l in range(min(f_y, t_y), max(f_y, t_y)+1,1):
                grid[l][k] = '#'
        elif f_x != t_x and f_y == t_y:
            l = f_y
            for k in range(min(f_x, t_x), max(f_x, t_x)+1,1):
                grid[l][k] = '#'
        else:
            for k in range(min(f_x, t_x), max(f_x, t_x)+1,1):
                for l in range(min(f_y, t_y), max(f_y, t_y)+1,1):
                    grid[l][k] = '#'
grid[-1] = ['#' for _ in range((max_y+3)*2)]

for line in grid:
    print(line)
# pprint.pprint(grid)   

# #Find position of 500 in grid.
# # [row, column] 

start = [0, 500-min_x+half_y]

#Start dropping sand
#grid[r][c], moving down changes r. 
#Move down, or diagonal left, or diagonal right.
#Else, stay. 

DIR = [(1,0),(1,-1),(1,1)]

[r,c] = start
z, q = True, True
sand = 0

while z:
    sand += 1
    [r,c] = start
    q = True
    if grid[r][c] == 'o':
        q = False
        z = False
        break
    grid[r][c] = 'o'
    while q:
        # for line in grid:
        #     print(line)
        for dr,dc in DIR:
            rr = r + dr
            cc = c + dc
            #print('rr', rr, 'cc', cc)
            if grid[rr][cc] == '.':
                grid[rr][cc] = 'o'
                grid[r][c] = '.'
                [r,c] = [rr,cc]
                # pprint.pprint(grid)  
                break
            elif (dr,dc) == (1,1):
                q = False
                break

# pprint.pprint(grid)
# for line in grid:
#     print(line)

print('Total sand:', sand-1)



        

    



#input[list][number in list[x,y]]
#input[row] [column]
# (0,0) (0,1)
# (1,0) (1,1)

