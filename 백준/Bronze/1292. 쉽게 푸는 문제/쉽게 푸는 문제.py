A, B = map(int, input().split())
arr = []
num = 1
count = 0
for i in range(B):
    arr.append(num)
    count += 1
    if count == num:
        count = 0
        num += 1

print(sum(arr[A-1:B]))