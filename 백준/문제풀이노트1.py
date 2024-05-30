n = int(input())
pos = list(map(int, input().split()))
arr = sorted(set(pos))

dic = {arr[i]: i for i in range(len(arr))}

for i in pos:
    print(dic[i], end=' ')