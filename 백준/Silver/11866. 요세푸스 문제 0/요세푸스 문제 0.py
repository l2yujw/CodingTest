from collections import deque
from sys import stdin
input = stdin.readline
N, K = map(int, input().split())
arr = deque(i for i in range(1, N + 1))

count = 0
ans = []
while len(arr) != 0:
    if count == K -1:
        count = 0
        ans.append(str(arr.popleft()))
    else:
        arr.append(arr.popleft())
        count += 1

print("<" + ", ".join(ans) + ">")