n = int(input())

arr = []
for i in range(n):
    arr.append(list(map(int, input().split())))

arr.sort(key=lambda x:(x[1], x[0]))

ans = 0
end = 0
for s, e in arr:
    if end <= s:
        ans += 1
        end = e
print(ans)