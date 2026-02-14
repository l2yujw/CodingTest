from sys import stdin
input = stdin.readline

N = int(input())

lope = [int(input()) for _ in range(N)]
lope.sort(reverse=True)

result = []
for i in range(N):
    result.append(lope[i] * (i + 1))

print(max(result))