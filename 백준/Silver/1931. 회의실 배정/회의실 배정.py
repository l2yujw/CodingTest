from sys import stdin

input = stdin.readline
n = int(input())

arr = []
for _ in range(n):
    s, e = map(int, input().split())
    arr.append((e, s))

arr.sort()

end, _ = arr[0]
ans = 1
for e, s in arr[1:]:
    if s >= end:
        ans += 1
        end = e
print(ans)