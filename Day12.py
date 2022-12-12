import string

input = open("Day12-input.txt",'r').read().split()

#input[list][number in list]
#input[row] [column]
# (0,0) (0,1) (0,2) (0,3) (0,4) (0,5)
# (1,0) (1,1) (1,2) (1,3) (1,4) (1,5)
# (2,0) (2,1) (2,2) (2,3) (2,4) (2,5)

start = 'S'
end = 'E'

rows = len(input)
columns = len(input[0])
start_a = []

for r in range(rows):
    for c in range(columns):
        if input[r][c] == start:
            co_start = (r,c)
            input[r] = input[r].replace(start,'a')
        if input[r][c] == end:
            co_end = (r,c)
            input[r] = input[r].replace(end,'z')
        if input[r][c] == 'a':
            start_a.append((r,c))
            
print('Start:', co_start)
print('End:', co_end)

paths = start_a
visited = set(start_a)
locations = start_a

DIR =  [(1, 0), (-1, 0), (0, 1), (0, -1)]

is_valid = lambda s, e: string.ascii_letters.index(e) - string.ascii_letters.index(s) <= 1

i = True
count = 0
while i == True and len(locations) > 0:
    count += 1
    for (r,c) in locations[:]:
        for (dr,dc) in DIR:
            rr = r + dr
            cc = c + dc
            if (rr,cc) not in visited:
                if 0 <= rr < rows and 0 <= cc < columns:       
                    if is_valid(input[r][c], input[rr][cc]):
                        locations.append((rr,cc))
                        visited.add((rr,cc))
                        if (rr,cc) == co_end:
                            print('solution:', rr, cc)
                            i = False
        locations.remove((r,c))

print('Result =', count)


