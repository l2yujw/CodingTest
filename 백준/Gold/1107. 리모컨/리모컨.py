from sys import stdin

input = stdin.readline
N = int(input())
M = int(input())
el = list(map(int, input().split()))

minCount = abs(100 - N)

for x in range(1000001):
    x = str(x)
    
    for k in range(len(x)):
        if int(x[k]) in el:
            break
        
        elif k == len(x) - 1:
            minCount = min(minCount, abs(int(x) - N) + len(x))

print(minCount)