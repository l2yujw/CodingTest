T = int(input())
for test_case in range(1, T + 1):
	arr = [0] * 101
	n = int(input())
	score = list(map(int, input().split()))
	for i in score:
		arr[i] += 1

	result = []
	for k in range(len(arr)):
		if arr[k] == max(arr):
			result.append(k)
	print(f"#{n} {max(result)}")