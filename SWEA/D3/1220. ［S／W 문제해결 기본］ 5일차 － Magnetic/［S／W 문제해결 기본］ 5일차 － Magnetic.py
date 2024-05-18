T = 10
for test_case in range(1, T + 1):
	n = int(input())
	arr = [list(map(int, input().split())) for _ in range(n)]

	count = 0
	for i in range(n):
		check = False
		for k in range(n):
			if arr[k][i] == 1:
				check = True
			if check and arr[k][i] == 2:
				count += 1
				check = False

	print(f"#{test_case} {count}")