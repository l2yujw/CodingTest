n = int(input())
way = list(input().split())

move = [[0, -1], [0, 1], [1, 0], [-1, 0]]
direction = ['L', 'R', 'D', 'U']

start = [1, 1]

for i in way:
    for k in range(len(direction)):
        if direction[k] == i:
            ny = start[0] + move[k][0]
            nx = start[1] + move[k][1]
    if nx < 1 or ny < 1:
        continue

    start = [ny, nx]

# des = start
# print(des)
# des[0] = 4
# des[1] = 7
# print(start) =으로 배열을 같다하면 주소가 같아짐

print(start)