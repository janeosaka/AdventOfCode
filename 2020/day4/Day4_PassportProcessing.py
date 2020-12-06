def open_file():
    with open('../passport.txt') as f:
        passport_list = f.read()
    return passport_list


def part1():
    passport = open_file()
    passport = "".join(passport)
    req = {"byr", "iyr", "eyr", "hgt", "hcl", "ecl", "pid"}
    passports = passport.split('\n\n')
    valid = 0
    for entry in passports:
        field_keys = {field.split(":")[0] for field in entry.split()}
        if field_keys & req == req:
            valid += 1

