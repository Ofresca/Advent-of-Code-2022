"""
Day 07 of Advent of Code
"""

input = open("Day07-input.txt",'r').read().split('\n')

def next_dollar(i):
    while i < len(input):
        i = i+1
        if i == len(input):
            return i
        line = input[i]
        if line[0] == '$':
            return i

# def amount_dir(i):
#     last = next_dollar(i)
#     count = 0
#     for idx in range(i,last):
#         line = input[idx]
#         if line[0:3] == 'dir':
#             count = count + 1
#     return count

def direct_dir(i, cur_dir):
    last = next_dollar(i)
    all_dir = [cur_dir]
    for idx in range(i,last):
        line = input[idx]
        if line[0:3] == 'dir':
            all_dir.append(cur_dir + line[4:] + '/')
    return all_dir


dir = {}
loc = []
# order = 0

i = 0

#No need to read the first line.
cur_dir = '/'
dir[cur_dir] = 0

while i < len(input):
    i += 1
    if i == len(input):
        break
    line = input[i]
    if line[0] == '$':
        if line[2:4] == 'cd':
            #Change directory
            cur_dir += line[5:] + '/'
            if line[5:] == '..':
                cur_dir = '/'.join(cur_dir.split('/')[:-3]) + '/'
                # order -= 1
                #Move out one directory
                #Switch to outmost directory
            elif cur_dir not in dir:
                dir[cur_dir] = 0
            # order += 1
        if line[2:4] == 'ls':
            # amount_dir(i)
            loc.append(direct_dir(i, cur_dir))
            #Creates a list of directories
            for idx in range(i+1, next_dollar(i)):
                line = input[idx]
                if line[0:3] == 'dir':
                    'do nothing'
                    #This directory is in current dir.
                else:
                    #We have found a file!
                    all = line.split(' ')
                    #Add size to size of directory.
                    dir[cur_dir] += int(all[0])
            i = next_dollar(i-1)

for dir_list in loc[::-1]:
    if len(dir_list) > 1:
        for extra_d in dir_list[1:]:
            dir[dir_list[0]] += dir[extra_d]

total = 0
for key in dir:
    if dir[key] <= 100000:
        total += dir[key]

print(total)

free_space = 70000000-dir['/']
need_space = 30000000
missing_space = need_space - free_space

print(missing_space)

min = missing_space
c_c = 0
for key in dir:
    if dir[key] >= missing_space and dir[key] - missing_space < min:
        min = dir[key] - missing_space
        c_c = dir[key]

print(c_c)

        
