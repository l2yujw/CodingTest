from sys import stdin

input = stdin.readline
N = int(input())

arr = [list(input().rstrip()) for _ in range(N)]

for x in arr:
    start = 0
    for k in x:
        if k == '(':
            start += 1
        else:
            start -= 1
        if start < 0:
            break
    if start != 0:
        print("NO")
    else:
        print("YES")