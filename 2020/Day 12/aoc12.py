fh = open('aoc12.txt')
data = [(line.strip()) for line in fh]
# degrees = 90
# value = [0, 0]
waypoint = [10, 1]
ship = [0, 0]

# for instruction in data:
#     if degrees == 90:
#         if instruction[0] == 'F':
#             value[0] += int(instruction[1:])
#         elif instruction[0] == 'N':
#             value[1] += int(instruction[1:])
#         elif instruction[0] == 'S':
#             value[1] -= int(instruction[1:])
#         elif instruction[0] == 'E':
#             value[0] += int(instruction[1:])
#         elif instruction[0] == 'W':
#             value[0] -= int(instruction[1:])
#         elif instruction[0] == 'L':
#             degrees -= int(instruction[1:])
#             if degrees >= 360:
#                 degrees -= 360
#             elif degrees < 0:
#                 degrees += 360
#         elif instruction[0] == 'R':
#             degrees += int(instruction[1:])
#             if degrees >= 360:
#                 degrees -= 360
#             elif degrees < 0:
#                 degrees += 360
#     elif degrees == 180:
#         if instruction[0] == 'F':
#             value[1] -= int(instruction[1:])
#         elif instruction[0] == 'N':
#             value[1] += int(instruction[1:])
#         elif instruction[0] == 'S':
#             value[1] -= int(instruction[1:])
#         elif instruction[0] == 'E':
#             value[0] += int(instruction[1:])
#         elif instruction[0] == 'W':
#             value[0] -= int(instruction[1:])
#         elif instruction[0] == 'L':
#             degrees -= int(instruction[1:])
#             if degrees >= 360:
#                 degrees -= 360
#             elif degrees < 0:
#                 degrees += 360
#         elif instruction[0] == 'R':
#             degrees += int(instruction[1:])
#             if degrees >= 360:
#                 degrees -= 360
#             elif degrees < 0:
#                 degrees += 360
#     elif degrees == 270:
#         if instruction[0] == 'F':
#             value[0] -= int(instruction[1:])
#         elif instruction[0] == 'N':
#             value[1] += int(instruction[1:])
#         elif instruction[0] == 'S':
#             value[1] -= int(instruction[1:])
#         elif instruction[0] == 'E':
#             value[0] += int(instruction[1:])
#         elif instruction[0] == 'W':
#             value[0] -= int(instruction[1:])
#         elif instruction[0] == 'L':
#             degrees -= int(instruction[1:])
#             if degrees >= 360:
#                 degrees -= 360
#             elif degrees < 0:
#                 degrees += 360
#         elif instruction[0] == 'R':
#             degrees += int(instruction[1:])
#             if degrees >= 360:
#                 degrees -= 360
#             elif degrees < 0:
#                 degrees += 360
#     elif degrees == 0:
#         if instruction[0] == 'F':
#             value[1] += int(instruction[1:])
#         elif instruction[0] == 'N':
#             value[1] += int(instruction[1:])
#         elif instruction[0] == 'S':
#             value[1] -= int(instruction[1:])
#         elif instruction[0] == 'E':
#             value[0] += int(instruction[1:])
#         elif instruction[0] == 'W':
#             value[0] -= int(instruction[1:])
#         elif instruction[0] == 'L':
#             degrees -= int(instruction[1:])
#             if degrees >= 360:
#                 degrees -= 360
#             elif degrees < 0:
#                 degrees += 360
#         elif instruction[0] == 'R':
#             degrees += int(instruction[1:])
#             if degrees >= 360:
#                 degrees -= 360
#             elif degrees < 0:
#                 degrees += 360
#
# print(abs(value[0]) + abs(value[1]))

def fn_for_waypoint(waypoint, a, b):
    if a == 'N':
        waypoint[1] += b
    elif a == 'S':
        waypoint[1] -= b
    elif a == 'E':
        waypoint[0] += b
    elif a == 'W':
        waypoint[0] -= b
    elif a == 'R':
        if b == 90:
            waypoint[0], waypoint[1] = waypoint[1], -waypoint[0]
        elif b == 180:
            waypoint[0], waypoint[1] = -waypoint[0], -waypoint[1]
        elif b == 270:
            waypoint[0], waypoint[1] = -waypoint[1], waypoint[0]
        else:
            pass
    elif a == 'L':
        if b == 90:
            waypoint[0], waypoint[1] = -waypoint[1], waypoint[0]
        elif b == 180:
            waypoint[0], waypoint[1] = -waypoint[0], -waypoint[1]
        elif b == 270:
            waypoint[0], waypoint[1] = waypoint[1], -waypoint[0]
        else:
            pass
    return waypoint

print(data)

for i in range(len(data)):
    a = data[i][0]
    b = int(data[i][1:])
    if a != 'F':
        waypoint = fn_for_waypoint(waypoint, a, b)
    else:
        for i in range(len(waypoint)):
            copy = waypoint.copy()
            copy[i] *= b
            ship[i] += copy[i]

print(abs(ship[0]) + abs(ship[1]))
