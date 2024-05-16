for test_case in range(1, 11):
    n = int(input())
    arr = list(map(int, input().split()))
    result = 0
    for i in range(2, n - 2):
        left = max(arr[i-2:i])
        right = max(arr[i+1:i+3])
        if left >= arr[i] or right >= arr[i]:
            continue
        else:
            result += arr[i] - max(left, right)
    print(f"#{test_case} {result}")