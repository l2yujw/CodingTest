T = int(input())
for test_case in range(1, T + 1):
    N = int(input())
    arr = ""
    for i in range(N):
        a, n = map(str, input().split())
        arr += a * int(n)

    print(f"#{test_case}")
    for k in range(len(arr) // 10 + 1):
        print(arr[10 * k: 10 * k + 10])