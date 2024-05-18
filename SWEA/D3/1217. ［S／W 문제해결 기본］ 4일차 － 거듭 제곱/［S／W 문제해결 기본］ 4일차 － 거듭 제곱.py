def mul(num, n):
    if n == 0:
        return 1
    return num * mul(num, n - 1)

T = 10
for test_case in range(1, T + 1):
	tc = int(input())
	n, m = map(int, input().split())
	print(f"#{test_case} {mul(n, m)}")