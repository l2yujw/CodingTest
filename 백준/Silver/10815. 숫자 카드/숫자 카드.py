N = int(input())
cards = list(map(int, input().split()))

arr = {}
for c in cards:
    arr[c] = arr.get(c, 0) + 1

M = int(input())
queries = list(map(int, input().split()))
answer = []
for q in queries:
    answer.append(arr.get(q, 0))

print(*answer)