import sys

input = sys.stdin.readline
N, K = map(int, input().split())
schedule = list(map(int, input().split()))

code = []
change = 0

#스케쥴을 미리 쫙 뽑아서 예상해서 교체해야함
for x in range(K):
    if schedule[x] in code:
        continue

    if len(code) < N:
        code.append(schedule[x])
        continue

    priority = []
    for k in code:
        if k in schedule[x:]:
            priority.append(schedule[x:].index(k))
        else:
            priority.append(101)
    target = priority.index(max(priority))
    code.remove(code[target])
    code.append(schedule[x])
    change += 1

print(change)