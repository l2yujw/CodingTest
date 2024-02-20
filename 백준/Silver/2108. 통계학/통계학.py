from sys import stdin
input = stdin.readline
N = int(input())

arr = []
count = dict()
for _ in range(N):
    x = int(input())
    arr.append(x)
    if x not in count:
        count[x] = 1
    else:
        count[x] += 1
arr.sort()

print(round(sum(arr)/N))
print((arr[N // 2]))

freq = max(count.values())
numbers = []
for key, value in count.items():
    if value == freq:
        numbers.append(key)
if len(numbers) == 1:
    print(numbers[0])
else:
    print(sorted(numbers)[1])

print(arr[-1] - arr[0])