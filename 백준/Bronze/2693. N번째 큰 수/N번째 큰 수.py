from sys import stdin
input = stdin.readline
T = int(input())

A = list([0]*10)
result=[]
N=3

for _ in range(T):
    A = sorted(list(map(int, input().split())))
    result.append(A[-N])

print(*result, sep="\n")