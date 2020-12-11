# fh = open('aoc10sample.txt')
# data = [int(line.strip()) for line in fh]
# outlet = 0
# differences = {}
# sorted = sorted(data)
#
# # for j in range(len(data)):
# #     if j == len(data) - 1:
# #         differences[3] = differences.get(3, 0) + 1
# #     for i in range(1,4):
# #         if outlet+i not in data:
# #             continue
# #         differences[i] = differences.get(i, 0) + 1
# #         outlet += i
# #         break
# # print(differences)
# # print(differences[1] * differences[3])
#
# list = [0] + sorted + [max(data) + 3]
# print(list)
# ways = 0
# tree = []
# for i in range(0, len(list)):
#     tree.append(list[i])
#     if list[i] == max(list):
#         print(ways)
#         break
#     if list[i]+1 in list:
#         continue
#     if list[i]+2 in list:
#         continue
#     if list[i]+3 in list:
#         if len(tree) == 4:
#             ways *= 4
#         else:
#             ways *= len(tree) - 1
#         tree = []
#         tree.append(list[i])

f = [int(i) for i in open("aoc10sample.txt").read().splitlines()]
f = [0] + f + [max(f)+3]
### Part 1 ###
f.sort()
print(f)
# a = [i for i in range(len(f)-1) if f[i+1]==(f[i]+1)]
# b = [i for i in range(len(f)-1) if f[i+1]==(f[i]+3)]
# print(len(a)*len(b))
### Part 2 ###
l = len(f)
ways = [1] + [0]*(l-1)
print(ways)
for i in range(1,l):
    ways[i] = sum((ways[o] for o in range(i-3,i) if f[i] <= (f[o]+3)))
print(ways[-1])






