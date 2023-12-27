N = int(input())
num = list(map(int, input().split()))

maxNum = num[0]
minNum = num[0]

for i in range(len(num)):
    if num[i] > maxNum:
        maxNum = num[i]
    elif num[i] < minNum:
        minNum = num[i]

print(minNum, maxNum)