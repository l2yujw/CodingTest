N = int(input())
OX = list(input().rstrip() for _ in range(N))

for y in range(N):
    count, res = 0, 0
    for x in OX[y]:
        if x == 'O':
            count += 1
        else:
            res += count * (count + 1) // 2
            count = 0
    res += count * (count + 1) // 2
    print(res)