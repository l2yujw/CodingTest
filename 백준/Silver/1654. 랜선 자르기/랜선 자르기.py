import sys

K, N = map(int, sys.stdin.readline().split())
lines = [int(input()) for _ in range(K)]

def binary_search():
    left, right = 1, max(lines)

    while left < right:
        mid = (left + right + 1) // 2

        count = sum(l // mid for l in lines)

        if count >= N:
            left = mid
        else:
            right = mid - 1

    return left

print(binary_search())