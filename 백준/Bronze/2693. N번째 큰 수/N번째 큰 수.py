T = int(input())

A = list([0]*10)
result=[]
N=3

for _ in range(T):
    A = list(map(int, input().split(" ")))
    A.sort()
    result.append(A[-N])

print(*result, sep="\n")