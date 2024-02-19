import sys

T = int(input())

N = []

input = sys.stdin.readline
for i in range(0, T) :
    N.append(input())

N.sort(key=lambda x: int(x.split()[0]))

print(''.join(N))