from sys import stdin
input = stdin.readline

N = int(input())
target = [0] * 10001
for _ in range(N):
    target[int(input())] += 1

for i in range(1, 10001):
    if target[i] >= 1:
        for _ in range(target[i]):
            print(i)