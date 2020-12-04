import string

fh = open('aoc4.txt')
verify = {}
list = []

for line in fh:
    line = line.split()
    if len(line) == 0:
        list.append(verify)
        verify = {}
        continue
    for i in range(len(line)):
        data = line[i].split(':')
        verify[data[0]] = data[1]

list.append(verify)



valid = 0

for i in range(len(list)):
    if not (len(list[i])) >= 7:
        continue
    if len(list[i]) == 7 and ('cid' in list[i]):
        continue
    if len((list[i])['byr']) != 4:
        continue
    if int((list[i])['byr']) < 1920 or int((list[i])['byr']) > 2002:
        continue
    if len((list[i])['iyr']) != 4:
        continue
    if int((list[i])['iyr']) < 2010 or int((list[i])['iyr']) > 2020:
        continue
    if len((list[i])['eyr']) != 4:
        continue
    if int((list[i])['eyr']) < 2020 or int((list[i])['eyr']) > 2030:
        continue
    if not 'cm' in (list[i])['hgt'] and not 'in' in (list[i])['hgt']:
        continue
    if 'cm' in (list[i])['hgt']:
        centi = ((list[i])['hgt']).strip('cm')
        if int(centi) < 150 or int(centi) > 193:
            continue
    if 'in' in (list[i])['hgt']:
        inch = ((list[i])['hgt']).strip('in')
        if int(inch) < 59 or int(inch) > 76:
            continue
    if not ((list[i])['hcl']).startswith('#'):
        continue
    if len((list[i])['hcl']) != 7:
        continue
    hcl_test = True
    for char in ((list[i])['hcl'])[1:]:
        if char.isnumeric():
            continue
        else:
            if not char in string.ascii_lowercase[:6]:
                hcl_test = False
                break
    if not hcl_test:
        continue
    eye_colour = ['amb', 'blu', 'brn', 'gry', 'grn', 'hzl', 'oth']
    if (list[i])['ecl'] not in eye_colour or len((list[i])['ecl']) != 3:
        continue
    if len((list[i])['pid']) != 9:
        continue
    pid_test = True
    for char in (list[i])['pid']:
        if char.isnumeric():
            continue
        else:
            pid_test = False
            break
    if not pid_test:
        continue
    valid += 1
    print(list[i])

print(valid)