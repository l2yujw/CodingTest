from sys import stdin

input = stdin.readline
n = int(input())

soo = []
pos = 0
for _ in range(n):
    soo.append(int(input()))

arr = []
answer = []
for x in range(1, n + 1):
    arr.append(x)
    answer.append('+')
    while True:
        if len(arr) != 0:
            tmp = arr.pop()
        else:
            break
        if tmp == soo[pos]:
            answer.append('-')
            pos += 1
        else:
            arr.append(tmp)
            break

if len(arr) == 0:
    print("\n".join(answer))
else:
    print("NO")