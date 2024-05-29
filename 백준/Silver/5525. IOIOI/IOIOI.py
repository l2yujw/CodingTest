n = int(input())
m = int(input())
s = list(input())

p = ['I', 'O', 'I']

for i in range(1, n):
    p.append('O')
    p.append('I')

ans = 0
for i in range(0, m - len(p) + 1):
    if s[i:i + len(p)] == p:
        ans += 1

print(ans)