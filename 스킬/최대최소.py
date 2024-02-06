import sys
ans = sys.maxsize

ans = sys.maxsize
arr = [5,4,3,2,1]
for num in arr:
    if ans > num:
        ans = num
print(ans)