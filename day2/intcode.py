f = open("day2\input.txt", "r")
codes = [int(i) for i in next(f).split(',')]

def run_program(noun, verb, codes):
    codes[1] = noun
    codes[2] = verb
    for i in range(len(codes) - 1):    
        if i % 4 == 0:
            opcode = codes[i]
            if opcode == 1: # addition
                codes[codes[i + 3]] = codes[codes[i + 1]] + codes[codes[i + 2]]
            elif opcode == 2: # multiplication
                codes[codes[i + 3]] = codes[codes[i + 1]] * codes[codes[i + 2]]
            elif opcode == 99: # halting
                break
    return codes

# part1
print(run_program(12, 2, codes))
