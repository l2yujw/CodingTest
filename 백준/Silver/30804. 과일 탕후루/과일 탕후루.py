import sys
input = sys.stdin.readline

N = int(input())
arr = list(map(int, input().split()))

counts = {}
left = 0
answer = 0

for right in range(N):
    num = arr[right]
    counts[num] = counts.get(num, 0) + 1

    while len(counts) > 2:
        left_num = arr[left]
        counts[left_num] -= 1
        if counts[left_num] == 0:
            del counts[left_num]
        left += 1

    answer = max(answer, right - left + 1)

print(answer)