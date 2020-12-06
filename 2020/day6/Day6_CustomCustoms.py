import string


def open_file():
    with open('../customs.txt', 'r') as f:
        answer_list = f.read().split('\n')
    return answer_list


def part1():
    answer_list = open_file()
    count = 0
    set_list = set()
    for answer in answer_list:
        if answer:
            set_list.__ior__(set(answer))
        else:
            count += len(set_list)
            set_list.clear()
    count += len(set_list)
    return count


def part2():
    answer_list = open_file()
    valid = []
    set_list = set()
    set_list.update(string.ascii_lowercase)
    temp_setlist = set_list
    for i in answer_list:
        if i.strip() == '':
            valid.append(temp_setlist)
            temp_setlist = set_list
        else:
            temp_setlist = temp_setlist.intersection(i.strip())
    return sum([len(x) for x in valid])
