from sys import stdin

input = stdin.readline
N = int(input())
primeNum = list(map(int, input().split()))
count = 0
for num in primeNum:
    if num == 1:
        continue

    for x in range(2, num):
        if num % x == 0:
            break

    else:
        count += 1

print(count)