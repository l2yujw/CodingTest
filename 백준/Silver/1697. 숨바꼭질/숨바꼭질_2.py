# 수빈 N 동생 K
# 수빈 x일때 걸으면 1초후 x-1 or x+1 순간이동미녀 1초후 2*x위치로 이동
# 수빈이와 동생의 위치가 주어졌을때 수빈이가 동생을 찾을 수 이쓴ㄴ 가장 빠른시간
#ex 5 17 / 4 ->5 10 15 2
from sys import stdin
input = stdin.readline

n, k = map(int, input().split())

arr = [0] * (k + 1)
for i in range(1, n):
    arr[i] = n - i

for i in range(n + 1, k + 1):
    prev = arr[i - 1] + 1
    if i % 2 == 1:
        left = arr[i // 2] + 2
        right = arr[i // 2 + 1] + 2
        arr[i] = min(left, right, prev)
    else:
        left = arr[i // 2] + 2
        right = arr[i // 2 + 1] + 2
        mid = arr[i // 2] + 1
        arr[i] = min(left, right, mid, prev)

print(arr[k])

#런타임 오류남