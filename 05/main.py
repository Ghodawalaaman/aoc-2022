sample = open("sample.txt", "r").read()
final_input = open("input.txt", "r").read()

def part1(Input):

    Input = Input.split('\n\n')
    stack_input = Input[0]
    moves = Input[1].split('\n')
    stack_input_lines = stack_input.split('\n')
    num_of_stack = len(stack_input_lines[len(stack_input_lines)-1].split('   ')) # not the best solution to find the number of the stack
    stack_input_lines.pop() # popping out the last unessential line

    stacks = []

    for _ in range(num_of_stack):
        stacks.append([])

    for line in stack_input_lines:
        line = line.split(' ')
        i = 0
        si = 0 # stack index
        while i < len(line):
            if line[i] == '':
                i += 4
                si += 1
                continue
            stacks[si].append(line[i][1])
            i += 1
            si += 1
        si += 1
    for stack in stacks:
        stack.reverse()

    # rearranging the stack
    for move in moves:
        move_info = move.split(' ')
        cnt = int(move_info[1])
        From = int(move_info[3])
        to = int(move_info[5])
        for _ in range(cnt): stacks[to-1].append(stacks[From-1].pop())

    ans = [stacks[i].pop() for i in range(num_of_stack)]
    return ''.join(ans)

def part2(Input):

    Input = Input.split('\n\n')
    stack_input = Input[0]
    moves = Input[1].split('\n')
    stack_input_lines = stack_input.split('\n')
    num_of_stack = len(stack_input_lines[len(stack_input_lines)-1].split('   ')) # not the best solution to find the number of the stack
    stack_input_lines.pop() # popping out the last unessential line

    stacks = []

    for _ in range(num_of_stack):
        stacks.append([])

    for line in stack_input_lines:
        line = line.split(' ')
        i = 0
        si = 0 # stack index
        while i < len(line):
            if line[i] == '':
                i += 4
                si += 1
                continue
            stacks[si].append(line[i][1])
            i += 1
            si += 1
        si += 1
    for stack in stacks:
        stack.reverse()

    # rearranging the stack
    for move in moves:
        move_info = move.split(' ')
        cnt = int(move_info[1])
        From = int(move_info[3])
        to = int(move_info[5])
        stacks[to-1] = stacks[to-1] + stacks[From-1][len(stacks[From-1])-cnt:]
        stacks[From-1] = stacks[From-1][0:len(stacks[From-1])-cnt]

    ans = [stacks[i].pop() for i in range(num_of_stack)]
    return ''.join(ans)

print("part1 (sample input) :",part1(sample))
print("part1 (final input)  :",part1(final_input))
print("part2 (sample input) :",part2(sample))
print("part2 (final input)  :",part2(final_input))
