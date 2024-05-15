arr = [50000, 10000, 5000, 1000, 500, 100, 50, 10]

T = int(input())
for test_case in range(1, T + 1):

	N = int(input())
	result = []
	for i in arr:
		result.append(N // i)
		N %= i

	print(f"#{test_case}")
	print(*result)