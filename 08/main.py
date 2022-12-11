import pprint

sample = open("sample.txt", "r").read()
final_input = open("input.txt", "r").read()


def scenic_score(grid,i,width,height):
    row = i//height
    col = i% height
    if row == 0 or row == height-1 or col == 0 or col == width-1: return 0
    left = grid[row*width + col-1:row*width-1:-1]
    right = grid[row*width + col+1:(row+1)*width]
    up = grid[i:col-1:-width]
    up.pop(0)
    down = grid[i:(width-1)*height + col+1:width]
    down.pop(0) # ignore the first element

    s = 1
    for x in (left,right,up,down):
        if len(x) == 1: continue
        tree = 0
        j = 0
        while j < len(x):
            if x[j] >= grid[i]:
                tree += 1
                break
            tree += 1
            j += 1
        s *= tree
    return s

def is_visible(grid,i,width,height):
    row = i//height
    col = i% height
    if row == 0 or row == height-1 or col == 0 or col == width-1: return True
    left = grid[row*width:row*width + col]
    right = grid[row*width + col+1:(row+1)*width]
    up = grid[col:i:width]
    down = grid[i:(width-1)*height + col+1:width]
    down.pop(0) # ignore the first element

    for x in (left,right,up,down):
        if grid[i] > max(x): return True
    return False

def part1(Input):
    grid = []
    linear_grid = []
    Input = list(filter(lambda x: x != '',Input.split('\n')))
    row = 0

    for line in Input:
        col = 0
        grid.append([])
        for h in line:
            grid[-1].append({'height':int(h),'visible':False})
            col += 1
        row += 1

    for line in Input:
        linear_grid += [*line]
    # Papa's solution
    s = 0
    for i in range(len(linear_grid)):
        if is_visible(linear_grid,i,col,row): s += 1
        pass

    return s

def part2(Input):
    grid = []
    linear_grid = []
    Input = list(filter(lambda x: x != '',Input.split('\n')))
    row = 0

    for line in Input:
        col = 0
        grid.append([])
        for h in line:
            grid[-1].append({'height':int(h),'visible':False})
            col += 1
        row += 1

    for line in Input:
        linear_grid += [*line]
    Max = -1
    index = -1
    for i in range(len(linear_grid)):
        score = scenic_score(linear_grid,i,col,row)
        if score > Max:
            Max = score
            index = i
        pass
    return Max

print("part1 (sample input) :",part1(sample))
print("part1 (final input)  :",part1(final_input))
print("part2 (sample input) :",part2(sample))
print("part2 (final input)  :",part2(final_input))
