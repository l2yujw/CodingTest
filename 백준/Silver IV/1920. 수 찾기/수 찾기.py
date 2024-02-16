from sys import stdin

input = stdin.readline
N = int(input())
A = list(map(int, input().split()))
A.sort()

M = int(input())
B = list(map(int, input().split()))

for x in B:
    start, end = 0, N - 1

    while start <= end:
        mid = (start + end) // 2
        if x > A[mid]:
            start = mid + 1
        elif x < A[mid]:
            end = mid - 1
        else:
            start = mid
            end = mid
            break
    if start == mid and end == mid:
        print(1)
    else:
        print(0)