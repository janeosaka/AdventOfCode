fh = open('aoc5.txt')
boarding_passes = []
seat_ids = []

for line in fh:
    line = line.strip()
    boarding_passes.append(line)

print('Number of passes: ', len(boarding_passes))

for i in range(len(boarding_passes)):
    upper_half = 128
    lower_half = 0
    right_seat = 8
    left_seat = 0
    for char in boarding_passes[i]:
        if char == 'F':
            guess = (upper_half + lower_half)/2
            upper_half = guess
        elif char == 'B':
            guess = (upper_half + lower_half)/2
            lower_half = guess
        elif char == 'R':
            guess_seat = (right_seat + left_seat)/2
            left_seat = guess_seat
        elif char == 'L':
            guess_seat = (right_seat + left_seat)/2
            right_seat = guess_seat
    row = min(upper_half, lower_half)
    column = min(right_seat, left_seat)
    id = row * 8 + column
    seat_ids.append(id)

print('Max is: ', max(seat_ids))
sorted = sorted(seat_ids)
for i in range(1, len(sorted)):
    if sorted[i] != sorted[i-1] + 1:
        print((sorted[i] + sorted[i-1])/2)