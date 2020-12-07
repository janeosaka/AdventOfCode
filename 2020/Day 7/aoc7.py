import string
import re

fh = open('aoc7.txt')
rules = []
list_of_bags = []
sum_of_inner_bags = {}
total_sum = {}

for line in fh:
    line = line.strip()
    rules.append(line)

for rule in rules:
    rule = rule.split(' contain ')
    to_sum = re.findall('[0-9]+', rule[1])
    sum = 0
    for i in range(len(to_sum)):
        sum += int(to_sum[i])
    sum_of_inner_bags[rule[0][:-1]] = sum

def recursion(colour):
    if sum_of_inner_bags[colour] == 0:
        return sum_of_inner_bags[colour]
    else:
        sum = 0
        for rule in rules:
            if rule.startswith(colour):
                rule = rule.split(' contain ')
                to_sum = re.findall('[0-9]+', rule[1])
                for i in range(len(to_sum)):
                    sum += int(to_sum[i])
                rule[1] = rule[1].split(', ')
                to_multiply = []
                for bag in rule[1]:
                    if bag == 'no other bags.':
                        break
                    if bag[-1] == 'g':
                        to_multiply.append(bag[2:])
                    elif bag[-2] == 'g':
                        to_multiply.append(bag[2:-1])
                    elif bag[-2] == 's':
                        to_multiply.append(bag[2:-2])
                for i in range(len(to_sum)):
                    sum += int(to_sum[i]) * recursion(to_multiply[i])

        total = sum
        return total

print(recursion('shiny gold bag'))


