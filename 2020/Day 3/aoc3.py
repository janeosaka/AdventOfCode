fh = open('aoc3.txt')
map = []
tree_or_square = []
k = 0
for line in fh:
    line = line.strip()
    map.append(line)

for i in range(len(map)):
    if i%2 != 0:
        continue
    char = map[i]
    try:
        tree_or_square.append(char[k])
    except:
        char = char * i
        tree_or_square.append(char[k])
    k += 1

tree = 0

for puzzle in tree_or_square:
    if puzzle == '#':
        tree += 1

print(tree)
print(len(tree_or_square))
print(tree_or_square)







