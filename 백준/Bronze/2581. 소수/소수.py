from sys import stdin

def prime(x) :
  for i in range(2,x) :
    if x%i == 0 :
      return 0
  return 1

input = stdin.readline
M = int(input())
N = int(input())
arr = []

for num in range(M, N+1):
    if num == 1:
        continue
    if prime(int(num)) == 1:
        arr.append(num)

if len(arr) != 0:
    print(sum(arr))
    print(arr[0])
else:
    print(-1)
