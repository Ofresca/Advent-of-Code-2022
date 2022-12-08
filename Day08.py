input = open("Day08-input.txt",'r').read().split()

height = len(input)
width = len(input[0])

vis_tree = 2*height + 2*(width-2)
invis_tree = 0

for x in range(1,width-1):
    for y in range(1,height-1):
        tree = input[x][y]

        if tree > max(input[x][(y+1):]):
            vis_tree += 1
        elif tree > max(input[x][:y]):
            vis_tree += 1
        elif tree > max([input[i][y] for i in range(x+1,height)]):
            vis_tree += 1
        elif tree > max([input[i][y] for i in range(0,x)]):
            vis_tree += 1
        else:
            invis_tree += 1

print('Part 1:', vis_tree)

max_tree_vis = 0

for x in range(1,width-1):
    for y in range(1,height-1):
        tree = int(input[x][y])

        trees_up = [int(input[h][y]) for h in range(x-1, -1, -1)]
        trees_down = [int(input[h][y]) for h in range(x+1, width)]
        trees_left = [int(input[x][w]) for w in range(y-1, -1, -1)]
        trees_right = [int(input[x][w]) for w in range(y+1, height)]

        tree_up = min(max([i+2 for i in range(len(trees_up)) if tree > max(trees_up[:i+1])] + [1]), len(trees_up))
        tree_down = min(max([i+2 for i in range(len(trees_down)) if tree > max(trees_down[:i+1])] + [1]), len(trees_down))
        tree_left = min(max([i+2 for i in range(len(trees_left)) if tree > max(trees_left[:i+1])] + [1]), len(trees_left))
        tree_right = min(max([i+2 for i in range(len(trees_right)) if tree > max(trees_right[:i+1])] + [1]), len(trees_right))

        trees = tree_up * tree_down * tree_left * tree_right
        if trees > max_tree_vis:
            max_tree_vis = trees

print('Part 2:', max_tree_vis)