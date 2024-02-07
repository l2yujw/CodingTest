from itertools import combinations
print(list(combinations([1, 2, 3, 4], 3)))

N, M = map(int, input().split())
arr = [str(i + 1) for i in range(N)]

for e in list(combinations(arr, M)):
    print(e)
    print(" ".join(e))