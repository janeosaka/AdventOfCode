def open_file():
    with open('aoc11.txt', 'r') as f:
        seat_layout = list(map(lambda x: x.rstrip(), f.readlines()))
    return seat_layout

def solve_for_occupied(ferry, x_move, y_move):
    x = y = 0
    string = ''
    copy = []
    while y < len(ferry):
        occupied = 0
        for i in [-1, 1]:
            if x+i < 0 or x+i == len(ferry[0]):
                continue
            if ferry[y][x+i] == '#':
                occupied += 1
        for i in [-1, 1]:
            if y+i < 0 or y+i == len(ferry):
                continue
            for j in [-1, 0, 1]:
                if x+j < 0 or x+j == len(ferry[0]):
                    continue
                if ferry[y+i][x+j] == '#':
                    occupied += 1
        if ferry[y][x] == 'L':
            if occupied == 0:
                string += '#'
            else:
                string += ferry[y][x]
        else:
            string += ferry[y][x]
        if len(string) == len(ferry[0]):
            copy.append(string)
            string = ''
        x += x_move
        y += y_move
        if x > 96:
            x = 0
            y += 1
    return copy

def solve_for_vacant(ferry, x_move, y_move):
    x = y = 0
    string = ''
    copy = []
    while y < len(ferry):
        occupied = 0
        for i in [-1, 1]:
            if x+i < 0 or x+i == len(ferry[0]):
                continue
            if ferry[y][x+i] == '#':
                occupied += 1
        for i in [-1, 1]:
            if y+i < 0 or y+i == len(ferry):
                continue
            for j in [-1, 0, 1]:
                if x+j < 0 or x+j == len(ferry[0]):
                    continue
                if ferry[y+i][x+j] == '#':
                    occupied += 1
        if ferry[y][x] == '#':
            if occupied >= 4:
                string += 'L'
            else:
                string += ferry[y][x]
        else:
            string += ferry[y][x]
        if len(string) == len(ferry[0]):
            copy.append(string)
            string = ''
        x += x_move
        y += y_move
        if x > 96:
            x = 0
            y += 1
    return copy

# round1 = solve_for_occupied(open_file(), 1, 0)
# round2 = solve_for_vacant(round1, 1, 0)
# round3 = solve_for_occupied(round2, 1, 0)
# round4 = solve_for_vacant(round3, 1, 0)
# round5 = solve_for_occupied(round4, 1, 0)

def recursion(old):
    new = solve_for_occupied(old, 1, 0)
    if new == old:
        print(old)
        print(new)
        return new
    else:
        old = solve_for_vacant(new, 1, 0)
        if old == new:
            print(old)
            print(new)
            return old
        else:
            return recursion(old)

round = recursion(open_file())
occupied = 0
for line in round:
    for char in line:
        if char == '#':
            occupied += 1

print(occupied)



