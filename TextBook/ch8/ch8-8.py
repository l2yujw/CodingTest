n, m = map(int, input().split())

arr = []
for _ in range(n):
    arr.append(int(input()))

arr.sort(reverse=True)
count = 0

for i in arr:
    if m % i == 0:
        count += m // i
        m -= i * (m // i)

if m == 0:
    print(count)
else:
    print(-1)