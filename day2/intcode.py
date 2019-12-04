from itertools import product

f = open("day2\input.txt", "r")
values = [int(i) for i in next(f).split(',')]

def run_program(noun, verb, codes):
    codes = values.copy()
    codes[1] = noun
    codes[2] = verb
    for i in range(0, len(codes), 4):    
        opcode = codes[i]
        if opcode == 1: # addition
            codes[codes[i + 3]] = codes[codes[i + 1]] + codes[codes[i + 2]]
        elif opcode == 2: # multiplication
            codes[codes[i + 3]] = codes[codes[i + 1]] * codes[codes[i + 2]]
        elif opcode == 99: # halting
            break
    return codes[0]

# part1
print(run_program(12, 2, values))

# part2
for noun, verb in product(range(0, 100), range(0, 100)):
    if run_program(noun, verb, values) == 19690720:
        print(100 * noun + verb)
        break
