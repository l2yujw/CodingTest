current_pos = input()
row = int(current_pos[1])
col = int(ord(current_pos[0]) - int(ord('a'))) + 1
count = 0

steps = [(-2, -1), (-2, 1), (-1, 2), (1, 2), (2, 1), (2, -1), (1, -2),(-1, -2)]

for step in steps:
    next_row = row + step[0]
    next_col = col + step[1]
    if next_row >= 1 and next_row <= 8 and next_col >= 1 and next_col <= 8:
        count += 1

print(count)