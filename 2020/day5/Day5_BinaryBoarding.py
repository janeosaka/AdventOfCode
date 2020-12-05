def open_file():
    with open('../seats.txt', 'r') as f:
        seat_list = f.readlines()
    return seat_list


def part1():
    seat_list = open_file()
    seats = []
    for record in seat_list:
        record = (record.replace('F', '0').replace('B', '1').replace('R', '1').replace('L', '0'))
        row = int(record[:7], 2)
        col = int(record[7:], 2)
        seat = (row * 8) + col
        seats.append(seat)
    print(max(seats))
    return sorted(seats)


print(part1())


# def part2():
#     seats = sorted(part1())
#     enumerate(seats)
#     for i, seat in seats:
#         if min(seats) < seat < max(seats):
#             if seats[i + 1] - seat == 2:
#                 return seat + 1
#             else:
#                 return 0
#
#
# print(part2())

def part2():
    seat_list = part1()
    for i, seats in enumerate(seat_list):
        if min(seat_list) < seats < max(seat_list):
            if seat_list[i + 1] - seats == 2:
                print(seats + 1)
                break


part2()
exit()
