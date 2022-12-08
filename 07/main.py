sample = open("sample.txt", "r").read()
final_input = open("input.txt", "r").read()

def mkdir(child_dir_name, parent_dir):
    parent_dir['childs'].append({'name':child_dir_name,'parent':parent_dir, 'dir_size':0,'childs':[], 'files':[]})
    return parent_dir['childs'][len(parent_dir['childs'])-1]

def cd(cur_dir, next_dir_name):
    if next_dir_name == "..": return cur_dir['parent']
    for child in cur_dir['childs']:
        if child['name'] == next_dir_name:
            return child
    return mkdir(next_dir_name, cur_dir)

def type_of_input(Input):
    Input = Input.split()
    if Input[0] == '$':
        if Input[1] == "cd": return "CD_COMMAND"
        if Input[1] == "ls": return "LS_COMMAND"
    else: return "DATA"


def calculate_dir_size(Dir):
    s = 0
    for child in Dir['childs']:
        s += calculate_dir_size(child)
    for files in Dir['files']:
        s += files['size']
    Dir['dir_size'] = s
    return s

def parse(Input):
    Input = list(filter(lambda x: x != '',Input.split('\n')))

    dirs = [{'name':"/",'parent':None,'dir_size':0, 'childs':[], 'files':[]}]
    cur_dir = dirs[0]
    i = 1
    while i < len(Input):
        tokens = Input[i].split()
        tokens_type = type_of_input(Input[i])
        if tokens[0] == '$':
            if tokens[1] == "cd":
                cur_dir = cd(cur_dir, tokens[2])
            elif tokens[1] == "ls":
                pass
            else:
                assert "UNKNOWN COMMAND"
        else:
            if tokens[0] == "dir":
                i += 1
                continue
            file_size = int(tokens[0])
            file_name = tokens[1]
            for file in cur_dir['files']:
                if file['name'] == file_name:
                    i += 1
                    continue
            cur_dir['files'].append({'name':file_name,'size':file_size})
        i += 1
    calculate_dir_size(dirs[0])
    return dirs

def solve1(Dir):
    s = 0
    for child in Dir['childs']:
        s += solve1(child)
    if Dir['dir_size'] <= 100000: s += Dir['dir_size']
    return s

def list_of_dirs(Dir):
    List = []
    for child in Dir['childs']:
        List += list_of_dirs(child)
        List.append(child)
    return List

def part1(Input):
    dirs = parse(Input)
    return solve1(dirs[0])

def part2(Input):
    dirs = parse(Input)
    List = [dirs[0]]
    List += list_of_dirs(dirs[0])
    List.sort(key=lambda l: l['dir_size'])
    TOTAL_SPACE = 70000000
    NEEDED_SPACE = 30000000
    AVAILABEL_SPACE = TOTAL_SPACE - List[-1]['dir_size']
    if NEEDED_SPACE < AVAILABEL_SPACE: assert "Maybe you don't want to delete anything huh?"
    for l in List:
        if l['dir_size'] >= (NEEDED_SPACE - AVAILABEL_SPACE): return l['dir_size']
    assert "UNREACHABLE: NO SOLUTION"

print("part1 (sample input) :",part1(sample))
print("part1 (final input)  :",part1(final_input))
print("part2 (sample input) :",part2(sample))
print("part2 (final input)  :",part2(final_input))
