n, k = map(int, input().split())
a = list(map(int, input().split()))
b = list(map(int, input().split()))

a.sort()
b.sort(reverse=True)

pos = 0
for i in range(k):
    if a[i] < b[pos]:
        a[i], b[pos] = b[pos], a[i]
        pos += 1
    else:
        break

print(sum(a))