from itertools import permutations

N, M = map(int, input().split())
arr = [str(i + 1) for i in range(N)]

for e in list(permutations(arr, M)):
    print(" ".join(e))