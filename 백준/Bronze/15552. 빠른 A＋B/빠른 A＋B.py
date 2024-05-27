from sys import stdin

input = stdin.readline

n = int(input().rstrip())
for _ in range(n):
    a, b = map(int, input().split())
    print(a + b)