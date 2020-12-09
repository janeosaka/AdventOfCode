def open_file():
    with open('../encode.txt', 'r') as f:
        encode_list = [int(x) for x in f.read().split()]
    return encode_list


def part1():
    encode_list = open_file()
    preamble_length = 25
    start = 0

    while preamble_length != len(encode_list):
        count = 0
        min_max = encode_list[start:preamble_length]
        for k in min_max:
            if encode_list[preamble_length] - k in min_max:
                count = 1
        if count == 0:
            return encode_list[preamble_length]
        start += 1
        preamble_length += 1


print(part1())


def part2():
    encode_list = open_file()
    tmp = part1()
    x = encode_list.index(tmp)
    for i in range(len(encode_list[:x])):
        for j in range(i):
            if sum(encode_list[j:i]) == tmp:
                return min(encode_list[j:i]) + max(encode_list[j:i])


print(part2())
