from sys import stdin

input = stdin.readline

S = int(input())

N = int(S**0.5)
while True:
    if N * (N + 1) / 2 > S:
        N -= 1
        break
    if N * (N + 1) / 2 == S:
        break
    N += 1
print(N)