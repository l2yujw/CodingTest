def find(start):
    if len(arr) == m:
        print(*arr)
        return
    for i in range(start, n + 1):
        arr.append(i)
        find(i + 1)
        arr.pop()


n, m = map(int, input().split())

arr = []
find(1)