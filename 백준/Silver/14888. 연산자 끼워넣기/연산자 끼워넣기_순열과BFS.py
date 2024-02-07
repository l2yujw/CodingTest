from sys import stdin
from itertools import permutations

input = stdin.readline
N = int(input())
A = list(map(int, input().split(" ")))
num = list(map(int, input().split(" ")))

oper = []
pos = 0
for x in num:
    for k in range(x):
        oper.append(pos)
    pos += 1

result = []
permutationList = list(permutations(oper, len(oper)))
for e in permutationList:
    sum = A[0]
    pos = 1
    for x in e:
        if x == 0:
            sum += A[pos]
        elif x == 1:
            sum -= A[pos]
        elif x == 2:
            sum *= A[pos]
        elif x == 3:
            if sum < 0:
                sum = -(abs(sum) // A[pos])
            else:
                sum //= A[pos]
        else:
            print("오류")
        pos += 1

    result.append(sum)

print(max(result))
print(min(result))