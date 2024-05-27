visited = [0] * 31
for _ in range(1, 29):
    visited[int(input())] = 1

for i in range(1, 31):
    if visited[i] == 0:
        print(i)