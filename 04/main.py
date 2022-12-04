sample = open("sample.txt", "r").read()
final_input = open("input.txt", "r").read()

def partially_overlaps(r1, r2):
    return True if r1[0] in range(r2[0], r2[1]+1) or r1[1] in range(r2[0], r2[1]+1) or r2[0] in range(r1[0], r1[1]+1) or r2[1] in range(r1[0], r1[1]+1) else False

def fully_overlaps(r1, r2):
    return (r1[0] <= r2[0] and r1[1] >= r2[1]) or (r1[0] >= r2[0] and r1[1] <= r2[1])

def part1(Input):
    pairs = list(filter(lambda x: x != '', Input.split('\n')))
    s = 0
    for pair in pairs:
        pair = pair.split(',')
        range1 = list(map(int,pair[0].split('-')))
        range2 = list(map(int,pair[1].split('-')))
        if fully_overlaps(range1, range2):
            s += 1
    return s

def part2(Input):
    pairs = list(filter(lambda x: x != '', Input.split('\n')))
    s = 0
    for pair in pairs:
        pair = pair.split(',')
        range1 = list(map(int,pair[0].split('-')))
        range2 = list(map(int,pair[1].split('-')))
        if partially_overlaps(range1, range2):
            s += 1
    return s

print("part1 (sample input) :",part1(sample))
print("part1 (final input)  :",part1(final_input))
print("part2 (sample input) :",part2(sample))
print("part2 (final input)  :",part2(final_input))
