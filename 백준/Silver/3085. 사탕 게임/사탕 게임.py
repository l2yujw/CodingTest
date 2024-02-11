from sys import stdin

input = stdin.readline

N = int(input())

# C P Z Y
arr = [list(input()) for _ in range(N)]
maxCount = 0

def solve():
    global arr
    for x in range(N):
        for kCol in range(N-1):
            if arr[x][kCol] == arr[x][kCol+1]:
                continue
            arr[x][kCol], arr[x][kCol+1] = arr[x][kCol+1], arr[x][kCol]
            findMax(arr)
            arr[x][kCol], arr[x][kCol + 1] = arr[x][kCol + 1], arr[x][kCol]

        for kRow in range(N - 1):
            if arr[kRow][x] == arr[kRow + 1][x]:
                continue

            arr[kRow][x], arr[kRow + 1][x] = arr[kRow + 1][x], arr[kRow][x]
            findMax(arr)
            arr[kRow][x], arr[kRow + 1][x] = arr[kRow + 1][x], arr[kRow][x]

def findMax(arr):
    global maxCount
    global N

    for x in range(N):
        count = 0
        for kRow in range(N - 1):
            cur = arr[x][kRow]
            count += 1
            if cur != arr[x][kRow+1]:
                maxCount = max(maxCount, count)
                count = 0
            elif kRow == N-2:
                count += 1
                maxCount = max(maxCount, count)

        count = 0
        for kCol in range(N - 1):
            cur = arr[kCol][x]
            count += 1
            if cur != arr[kCol + 1][x]:
                maxCount = max(maxCount, count)
                count = 0
            elif kCol == N-2:
                count += 1
                maxCount = max(maxCount, count)

solve()
print(maxCount)