import sys
input=sys.stdin.readline

N = int(input())
arr = []
for x in range(N):
    w, k = map(int, input().split())
    arr.append((w, k))

for k in arr:
    rank = 1
    for t in arr:
        if k[0] < t[0] and k[1] < t[1]:
            rank+=1
    print(rank, end=" ")