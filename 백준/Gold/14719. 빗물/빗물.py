from sys import stdin

input = stdin.readline

H, W= map(int, input().split())
num = list(map(int, input().split()))
ans = 0

for i in range(1, W-1):#1~3 1 2
    left_max = max(num[:i])
    right_max = max(num[i+1:])

    compare = min(left_max, right_max)

    if num[i] < compare:
        ans += compare - num[i]

print(ans)