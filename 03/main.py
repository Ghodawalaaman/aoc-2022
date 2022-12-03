sample = open("sample.txt", "r").read()
final_input = open("input.txt", "r").read()

def return_common(l1, l2):
    for e1 in l1:
        for e2 in l2:
            if e1 == e2:
                return e1

def calculate_sum_of_priority(l):
    s = 0
    for x in l:
        if ord(x) >= 97:
            s += ord(x) - 96
        else:
            s += ord(x) - 38
    return s

def part1(Input):
    common_items = []
    rucksacks = list(filter(lambda x : x != '', Input.split('\n')))
    for rucksack in rucksacks:
        comp1 = rucksack[0:(len(rucksack)//2)]
        comp2 = rucksack[len(rucksack)//2:]
        common_items.append(return_common(comp1,comp2))
    return calculate_sum_of_priority(common_items)

def part2(Input):
    badge = []
    rucksacks = list(filter(lambda x : x != '', Input.split('\n')))
    for i in range(0,len(rucksacks),3):
        for c in rucksacks[i]:
            if c in rucksacks[i+1]:
                if c in rucksacks[i+2]:
                    badge.append(c)
                    break
    return calculate_sum_of_priority(badge)

print("part1 (sample input) :",part1(sample))
print("part1 (final input)  :",part1(final_input))
print("part2 (sample input) :",part2(sample))
print("part2 (final input)  :",part2(final_input))
