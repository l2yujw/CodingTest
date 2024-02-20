import sys

def sort_num(a):
    x, y = a.split()
    return int(y) + int(x)/1000000

input=sys.stdin.readline
N = int(input())

arr = []
for _ in range(N):
    arr.append(input().strip())
arr.sort(key=lambda a: sort_num(a))

print(*arr, sep="\n")