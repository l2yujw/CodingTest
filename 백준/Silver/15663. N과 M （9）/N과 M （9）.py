def find():
    if len(res) == m:
        print(*res)
        return
    check = 0
    for i in range(n):
        if not visited[i] and check != arr[i]:
            visited[i] = True
            res.append(arr[i])
            check = arr[i]
            find()
            visited[i] = False
            res.pop()


n, m = map(int, input().split())
arr = sorted(list(map(int, input().split())))

res = []
visited = [False] * n
find()