fh = open('aoc8.txt')
instructions = []
for line in fh:
    line = line.strip()
    instructions.append(line)

def get_accelerator(i):
    global boolean
    if not i in used_instructions:
        if i == (len(instructions)-1):
            print('i for last instruction:', i)
            boolean = True
        used_instructions.append(i)
        count = 0
        instruction = copy[i].split()
        if instruction[0] == 'acc':
            if instruction[1][0] == '+':
                count += int(instruction[1][1:])
            else:
                count -= int(instruction[1][1:])
        elif instruction[0] == 'nop':
            pass
        elif instruction[0] == 'jmp':
            if instruction[1][0] == '+':
                return get_accelerator(i+(int(instruction[1][1:])))
            else:
                return get_accelerator(i-(int(instruction[1][1:])))
        global accelerator
        accelerator += count
        try:
            return get_accelerator(i+1)
        except:
            return accelerator
    else:
        print('Caught in infinite loop')
        boolean = False
        return accelerator

boolean = False
for i in range(len(instructions)):
    accelerator = 0
    copy = instructions.copy()
    used_instructions = []
    if instructions[i].startswith('jmp'):
        copy[i] = instructions[i].replace('jmp', 'nop')
    elif instructions[i].startswith('nop'):
        copy[i] = instructions[i].replace('nop', 'jmp')
    else:
        continue
    print(get_accelerator(0))
    if boolean != True:
        continue
    else:
        break

