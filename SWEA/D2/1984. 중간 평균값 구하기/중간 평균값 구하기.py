T = int(input())
for test_case in range(1, T + 1):
    arr = list(map(int, input().split()))
    arr.remove(max(arr))
    arr.remove(min(arr))

    print(f"#{test_case} {round(sum(arr) / len(arr))}")