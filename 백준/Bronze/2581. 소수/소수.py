from sys import stdin

def isPrime(x) :
  for i in range(2,int(x**0.5)+1) :
    if x%i == 0 :
      return False
  return True

input = stdin.readline
M = int(input())
N = int(input())
arr = []

for num in range(M, N+1):
    if num == 1:
        continue
    if isPrime(int(num)):
        arr.append(num)

if len(arr) == 0:
    print(-1)
else:
    print(sum(arr))
    print(arr[0])
