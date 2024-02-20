import sys
input=sys.stdin.readline

def round2(num):
    return int(num) + (1 if num - int(num) >= 0.5 else 0)

n = int(input())
if n:
    arr = [int(input()) for _ in range(n)]
    arr.sort()
    cutNum = round2(n * 0.15)
    print(round2(sum(arr[cutNum:-cutNum] if cutNum else arr) / (n - cutNum*2)))
else:
    print(0)
