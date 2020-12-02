# -*- coding: utf-8 -*-
"""
Created on Tue Dec  1 13:48:36 2020

@author: calvi
"""

sum = 0
fh = open('aoc1.txt', 'r')
numbers = []
found = False
for line in fh:
    line = line.strip()
    numbers.append(line)
numbers = [int(i) for i in numbers]
k = len(numbers)
    
# ----- PART ONE -----
# for i in range(len(numbers)):
#     for number in numbers:
#         if numbers[i] == number:
#             continue
#         if numbers[i] + number != 2020:
#             continue
#         else:
#             found = True
#             number1 = numbers[i]
#             number2 = number
#             answer = numbers[i] * number
#             break
#     if found:
#         print('Answer:', number1, '*', number2, 'is', answer)
#         break

for i in range(k):
    if found:
        break
    for j in range(k):
        if found:
            break
        for number in numbers:
            if numbers[i] == number or numbers[j] == number:
                continue
            if numbers[i] + numbers[j] + number != 2020:
                continue
            else:
                found = True
                number1 = numbers[i]
                number2 = numbers[j]
                number3 = number
                answer = number1 * number2 * number3
                break
            
print(number1, number2, number3)
