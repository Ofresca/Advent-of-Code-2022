import string

input = open("Day12-input.txt",'r').read().split()

#input[list][number in list]
#input[row] [column]
# (0,0) (0,1)
# (1,0) (1,1)

rows = len(input)
columns = len(input[0])
start_a = []

for r in range(rows):
    for c in range(columns):
        if input[r][c] == 'S':
            co_start = (r,c)
            input[r] = input[r].replace('S','a')
        elif input[r][c] == 'E':
            co_end = (r,c)
            input[r] = input[r].replace('E','z')
        if input[r][c] == 'a':
            start_a.append((r,c))
            
print('Start:', co_start)
print('End:', co_end)

# Part 1:
paths = [co_start]
visited = set({co_start})
locations = [co_start]

# Part 2:
paths = start_a
visited = set(start_a)
locations = start_a

is_valid1 = lambda rr, cc: 0 <= rr < rows and 0 <= cc < columns
is_valid2 = lambda sr, sc, er, ec : ord(input[er][ec]) - ord(input[sr][sc]) <= 1

i = True
count = 0
DIR =  [(1, 0), (-1, 0), (0, 1), (0, -1)]

while i == True and len(locations) > 0:
    count += 1
    for (r,c) in locations[:]:
        for (dr,dc) in DIR:
            rr = r + dr
            cc = c + dc
            if (rr,cc) not in visited and is_valid1(rr,cc) and is_valid2(r,c,rr,cc):
                locations.append((rr,cc))
                visited.add((rr,cc))
                if (rr,cc) == co_end:
                    print('Solution:', rr, cc)
                    i = False
        locations.remove((r,c))

print('Result =', count)


