import sys
input = sys.stdin.readline

N = int(input())
K = int(input())

left = 1
right = K
answer = 0

while left <= right:
    mid = (left + right) // 2
    
    count = 0
    for i in range(1, N + 1):
        count += min(N, mid // i)
    
    if count >= K:
        answer = mid
        right = mid - 1
    else:
        left = mid + 1

print(answer)