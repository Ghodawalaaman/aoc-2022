sample = open("sample.txt", "r").read()
final_input = open("input.txt", "r").read()

def part1(Input):
    Elf_foods = Input.split("\n\n")
    Elf_foods = list(filter(lambda x: x != '' and x != '\n',Elf_foods))


    total_calories = []
    for foods in Elf_foods:
        foods = foods.split("\n")
        foods = list(filter(lambda x: x != '',foods))
        s = 0
        for food in foods:
            calories = int(food)
            s += calories
        total_calories.append(s)

    return max(total_calories)

def part2(Input):
    Elf_foods = Input.split("\n\n")
    Elf_foods = list(filter(lambda x: x != '' and x != '\n',Elf_foods))


    total_calories = []
    for foods in Elf_foods:
        foods = foods.split("\n")
        foods = list(filter(lambda x: x != '',foods))
        s = 0
        for food in foods:
            calories = int(food)
            s += calories
        total_calories.append(s)

    # Calculating the sum of the top three Elves carrying maximum calories
    s = 0
    for i in range(3):
        max_calorie = max(total_calories)
        s += max_calorie
        total_calories.remove(max_calorie)
    return s

print("part1 (sample input) :",part1(sample))
print("part1 (final input)  :",part1(final_input))
print("part2 (sample input) :",part2(sample))
print("part2 (final input)  :",part2(final_input))
