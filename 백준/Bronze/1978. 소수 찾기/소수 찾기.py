from sys import stdin

def prime(x) :
  for i in range(2,x) :
    if x%i == 0 :
      return 0
  return 1

input = stdin.readline
N = int(input())
arr = input().split()
sum = 0
for i in arr :
  if i == '1' :
    continue
  sum += prime(int(i))
print(sum)