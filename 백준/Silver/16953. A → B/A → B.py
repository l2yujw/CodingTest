from sys import stdin
input = stdin.readline

a, b = map(int, input().split())

count = 1
while b > a:
    if b % 10 == 1:
        b = (b - 1) // 10
        count += 1
    elif b % 2 == 0:
        b //= 2
        count += 1
    else:
        break

print(count if b == a else -1)