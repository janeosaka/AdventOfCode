import random

fh = open('aoc9.txt')
strings = []
numbers = []
answer = 25918798
for line in fh:
    line = line.strip()
    strings.append(line)
numbers = [int(i) for i in strings]

# for i in range(25, len(numbers)):
#     previous = numbers[i-25:i]
#     found = 0
#     for x in range(len(previous)):
#         for y in range(x+1, len(previous)):
#             if int(previous[y]) == int(previous[x]):
#                 continue
#             if int(previous[y]) + int(previous[x]) == int(numbers[i]):
#                 found = 1
#                 break
#         if found == 1:
#             break
#     if found == 0:
#         print('Found the number', numbers[i])
#         break
found = 0
for i in range(len(numbers)):
    if found == 1:
        break
    set = []
    set.append(numbers[i])
    for j in range(i+1, len(numbers)):
        set.append(numbers[j])
        if sum(set) == answer:
            found = 1
            break
        elif sum(set) > answer:
            break
        else:
            continue

contiguous_set = max(set) + min(set)
print(contiguous_set)





