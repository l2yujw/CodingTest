from sys import stdin
input = stdin.readline

N = int(input())

dist = list(map(int, input().split()))
prices = list(map(int, input().split()))

result = 0
s = prices[0]

for i in range(N - 1):
    if prices[i] < s:
        s = prices[i]
    result += s * dist[i]

print(result)