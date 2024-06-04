def find():
    if len(res) == m:
        print(*res)
        return
    for i in range(n):
        if not visited[i]:
            res.append(arr[i])
            visited[i] = True
            find()
            visited[i] = False
            res.pop()


n, m = map(int, input().split())
arr = sorted(list(map(int, input().split())))

visited = [False] * n
res = []
find()