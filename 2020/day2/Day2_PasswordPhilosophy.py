def open_File():
    with open('../password.txt', 'r') as f:
        password_list = f.readlines()
    return password_list


def part1():
    password_list = open_File()
    valid = 0
    for parts in password_list:
        parts = parts.split(' ')
        char = parts[1].rstrip(":")
        if parts[2].find(char) != -1:
            freq = parts[2].count(char)
            char_range = parts[0].split("-")
            min_range = int(char_range[0])
            max_range = int(char_range[1])
            if min_range <= freq <= max_range:
                valid += 1
    print(valid)


def part2():
    password_list = open_File()
    valid = 0
    for parts in password_list:
        parts = parts.split(' ')
        char = parts[1].rstrip(":")
        if parts[2].find(char) != -1:
            char_pos = parts[0].split("-")
            check1 = parts[2][int(char_pos[0]) - 1]
            check2 = parts[2][int(char_pos[1]) - 1]
            if (check1 is char and check2 is not char) or (check1 is not char and check2 is char):
                valid += 1
    print(valid)


