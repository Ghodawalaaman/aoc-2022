sample = open("sample.txt", "r").read()
final_input = open("input.txt", "r").read()

elf_moves      = {'A':'ROCK', 'B':'PAPER', 'C':'SCISSORS'}
score          = {'ROCK':1, 'PAPER':2, 'SCISSORS':3}
lose_condition = {'ROCK':'SCISSORS', 'PAPER':'ROCK', 'SCISSORS':'PAPER'}
win_condition  = {'SCISSORS':'ROCK', 'ROCK':'PAPER', 'PAPER':'SCISSORS'}

def part1(Input):
    my_moves       = {'X':'ROCK', 'Y':'PAPER', 'Z':'SCISSORS'}
    rounds = list(filter(lambda x: x != '',Input.split('\n')))
    my_score = 0
    for r in rounds:
        moves       = r.split(' ')
        elf_move    = moves[0]
        my_move     = moves[1]
        if win_condition[my_moves[my_move]] == elf_moves[elf_move]:
            my_score += 6
        elif my_moves[my_move] == elf_moves[elf_move]:
            # draw
            my_score += 3
        my_score   += score[my_moves[my_move]]
    return my_score

def part2(Input):
    my_moves = {'X':'LOSE', 'Y':'DRAW', 'Z':'WIN'}
    my_score = 0
    rounds = list(filter(lambda x: x != '',Input.split('\n')))
    for r in rounds:
        moves       = r.split(' ')
        elf_move    = moves[0]
        game_ending = my_moves[moves[1]]
        if game_ending == 'WIN':
            my_score += 6
            my_move  = win_condition[elf_moves[elf_move]]
            my_score += score[my_move]
        elif game_ending == 'DRAW':
            my_score += 3
            my_move  = elf_moves[elf_move]
            my_score += score[my_move]
        elif game_ending == 'LOSE':
            my_score += 0
            my_move  = lose_condition[elf_moves[elf_move]]
            my_score += score[my_move]
    return my_score

print("part1 (sample input) :",part1(sample))
print("part1 (final input)  :",part1(final_input))
print("part2 (sample input) :",part2(sample))
print("part2 (final input)  :",part2(final_input))
