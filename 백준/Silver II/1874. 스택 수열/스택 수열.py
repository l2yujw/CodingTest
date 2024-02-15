from sys import stdin

input = stdin.readline
n = int(input())
soo = []
for _ in range(n):
    soo.append(int(input()))

def numeric():
    cnt, stack, result = 0, [], []
    for i in soo:
        while cnt < i:
            cnt += 1
            stack.append(cnt)
            result.append('+')
        if stack.pop() != i:
            return 'NO'
        else:
            result.append('-')
    return '\n'.join(result)

print(numeric())