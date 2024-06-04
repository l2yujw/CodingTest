def find(start):
    if len(res) == m:
        print(*res)
        return
    check = 0
    for i in range(start, n):
        if check != arr[i]:
            res.append(arr[i])
            check = arr[i]
            find(i)
            res.pop()


n, m = map(int, input().split())
arr = sorted(list(map(int, input().split())))

res = []
find(0)