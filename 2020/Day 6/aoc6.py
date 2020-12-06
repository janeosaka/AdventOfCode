fh = open('aoc6.txt')
group_answers = []
person_answers = {}
sum = 0
person = 0

# for line in fh:
#     line = line.strip()
#     if len(line) == 0:
#         group_answers.append(person_answers)
#         person_answers = ''
#     else:
#         person_answers += line
# group_answers.append(person_answers)
#
# print(group_answers)
#
# for answers in group_answers:
#     letters = []
#     for char in answers:
#         if not char in letters:
#             letters.append(char)
#     sum += len(letters)
#
# print(sum)

for line in fh:
    line = line.strip()
    if len(line) == 0:
        best = max(person_answers, key=lambda key: person_answers[key])
        if person_answers[best] != person:
            person_answers = {}
            person = 0
            continue
        else:
            group_answers.append(person_answers)
            person_answers = {}
            person = 0
    else:
        person += 1
        for char in line:
            person_answers[char] = person_answers.get(char, 0) + 1

best = max(person_answers, key=lambda key: person_answers[key])
if person_answers[best] == person:
    group_answers.append(person_answers)

for i in range(len(group_answers)):
    key_value = 0
    boolean = True
    if len(group_answers[i]) == 1:
        sum += 1
        continue
    for key in group_answers[i]:
        if key_value == 0:
            key_value = group_answers[i][key]
            continue
        if group_answers[i][key] == key_value:
            continue
        else:
            boolean = False
            break
    if boolean:
        sum += len(group_answers[i])
    if not boolean:
        key_value = 0
        for key in group_answers[i]:
            if group_answers[i][key] > key_value:
                n = 1
                key_value = group_answers[i][key]
                continue
            if group_answers[i][key] == key_value:
                n += 1
        sum += n
print(sum)