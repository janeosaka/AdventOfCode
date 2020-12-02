# -*- coding: utf-8 -*-
"""
Created on Wed Dec  2 13:58:22 2020

@author: calvi
"""

fh = open('aoc2.txt', 'r')
passwords = []
firstnum = []
secondnum = []
letter = []
password = []
count = 0

for line in fh:
    line = line.strip()
    passwords.append(line)

for x in passwords:
    dash = x.find('-')
    space = x.find(' ')
    colon = x.find(':')
    firstnum.append(x[0:dash])
    secondnum.append(x[dash+1:space])
    letter.append(x[colon-1:colon])
    password.append(x[colon+2:])
    
for i in range(len(password)):
    password[i] = '-' + password[i]
    
for i in range(len(password)):
    if letter[i] not in password[i]:
        continue
    k = password[i]
    if (k[int(firstnum[i])] == letter[i] and k[int(secondnum[i])] != letter[i]) or (k[int(firstnum[i])] != letter[i] and k[int(secondnum[i])] == letter[i]):
        count += 1
        
print(count)
        
        
        
        
    
    