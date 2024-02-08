from sys import stdin

input = stdin.readline
N ,S= map(int, input().split())
seq = list(map(int, input().split()))

minLen = 0
partSum = 0
tmpLen = 0
solvLen = 0
#최소길이 or 0

def solv():
    global partSum
    global tmpLen
    global minLen
    global solvLen

    for x in range(N):
        start = x
        partSum = 0
        tmpLen = 0
        while partSum < S:
            partSum += seq[start]
            tmpLen += 1

            if start == N-1 and partSum < S:
                tmpLen = minLen
                break
            elif start == N-1:
                break
            else:
                start += 1

        if solvLen == 0:
            minLen = tmpLen
        solvLen += 1
        minLen = min(minLen, tmpLen)

solv()
print(minLen)