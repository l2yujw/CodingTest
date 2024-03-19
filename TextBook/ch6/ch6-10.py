n = int(input())

arr = []
for _ in range(n):
    arr.append(input().rstrip())

arr = sorted(arr, reverse=True)

print(" ".join(arr))