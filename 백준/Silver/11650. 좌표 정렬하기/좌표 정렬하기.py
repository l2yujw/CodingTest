from sys import stdin
input = stdin.readline

N = int(input())

graph = []
for _ in range(N):
    graph.append(list(map(int, input().split())))

graph.sort(key=lambda x: (x[0], x[1]))

for g in graph:
    print(*g)
