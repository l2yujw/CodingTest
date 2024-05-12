def cal(n):
    if n == 1:
        return n
    if n % 2 == 1:
        return n + cal(n - 1)
    else:
        return -n + cal(n - 1)

T = int(input())
for test_case in range(1, T + 1):
    n = int(input())
    print("#%d %d" %(test_case, cal(n)))