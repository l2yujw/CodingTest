from sys import stdin
input = stdin.readline

n, m = map(int, input().split())

password = {a: b for a, b in [list(map(str, input().split())) for _ in range(n)]}
find = [input().rstrip() for _ in range(m)]

for i in range(m):
    print(password.get(find[i]))