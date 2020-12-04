def open_file():
    with open('../map.txt', 'r') as f:
        tree_map = list(map(lambda x: x.rstrip(), f.readlines()))
    return tree_map


def solve(forest, x_move, y_move):
    x = y = trees = 0
    while y < len(forest):
        if forest[y][x % len(forest[0])] == "#":
            trees += 1
        x += x_move
        y += y_move
    return trees


s0 = solve(open_file(), 3, 1)
s1 = solve(open_file(), 1, 1)
s2 = solve(open_file(), 5, 1)
s3 = solve(open_file(), 7, 1)
s4 = solve(open_file(), 1, 2)
print(s0)
print(s0 * s1 * s2 * s3 * s4)
