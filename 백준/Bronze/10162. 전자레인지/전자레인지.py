from sys import stdin
input = stdin.readline

T = int(input())
microwaves = [5 * 60, 1 * 60, 10]

answer = []
for m in microwaves:
    answer.append(T // m)
    T = T % m

if T == 0:
    print(*answer)
else:
    print(-1)