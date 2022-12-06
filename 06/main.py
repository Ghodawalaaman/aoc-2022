sample = open("sample.txt", "r").read()
final_input = open("input.txt", "r").read()

def have_dup(String):
    for c in String:
        cnt = 0
        for i in range(len(String)):
            if String[i] == c: cnt += 1
        if cnt != 1: return True
    return False

def solve(Input, marker_length, start):
    i = start
    while i < len(Input):
        c = Input[i]
        if not have_dup(Input[i:i+marker_length]):
            return i + marker_length
        i += 1
    return -1

def part1(Input):
    return solve(Input,4,0)

def part2(Input):
    return solve(Input,14,0)

print("part1 (sample input) :",part1(sample))
print("part1 (final input)  :",part1(final_input))
print("part2 (sample input) :",part2(sample))
print("part2 (final input)  :",part2(final_input))
