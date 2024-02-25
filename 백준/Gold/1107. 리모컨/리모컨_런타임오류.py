from sys import stdin

input = stdin.readline
N = list(map(int, str(input().rstrip())))
M = int(input())
if M != 0:
    broken = list(map(int, input().split()))
else:
    broken = []

availableNum = []
for i in range(10):
    if i in broken:
        continue
    else:
        availableNum.append(i)
print("availableNum", availableNum)
count = 0
findMinDiff = []
res = []
for x in N:
    if x in availableNum:
        count += 1
        res.append(x)
    else:
        if len(availableNum) != 0:
            diff = abs(x - availableNum[0])
            for k in range(1, len(availableNum)):
                check = abs(x - availableNum[k])
                if check < diff:
                    diff = min(diff, check)
            for k in range(0, len(availableNum)):
                check = abs(x - availableNum[k])
                if check == diff:
                    findMinDiff.append(availableNum[k])
            break
print("findMinDiff", findMinDiff)
finalNearNum = []
if len(findMinDiff) != 0:
    for r in findMinDiff:
        tmp = res.copy()
        if r < N[len(res)]:
            for _ in range(len(N) - len(res)):
                tmp.append(max(availableNum))
            finalNearNum.append(tmp)
        else:
            for _ in range(len(N) - len(res)):
                tmp.append(min(availableNum))
            finalNearNum.append(tmp)
if len(finalNearNum) != 0:
    count += len(finalNearNum[0]) - len(res)
print("finalNearNum", finalNearNum)

listsToInt = []
for y in finalNearNum:
    result = 0
    for x in range(len(y)):
        result += y[-x - 1]*(10**x)
    listsToInt.append(result)

print("listsToInt", listsToInt)

NToInt=[]
result = 0
for x in range(len(N)):
    result += N[-x - 1]*(10**x)
NToInt.append(result)
print("NToInt", NToInt)

if len(NToInt) != 0:
    minCount = abs(100 - NToInt[0])
    for i in range(len(listsToInt)):
        listsToInt[i] = abs(NToInt[0] - listsToInt[i])

if len(listsToInt) != 0:
    count += min(listsToInt)

print(min(minCount, count))