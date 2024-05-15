T = int(input())
for test_case in range(1, T + 1):
    n = int(input())
    arr = list(map(int, input().split()))
    count = 0
    for i in range(n):
        if arr[i] <= sum(arr) // n:
            count += 1
    print(f"#{test_case} {count}")