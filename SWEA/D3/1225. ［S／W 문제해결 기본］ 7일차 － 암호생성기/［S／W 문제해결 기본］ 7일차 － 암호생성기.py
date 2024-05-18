def cycle(arr, i):
    arr.append(arr.pop(0) - i)


for test_case in range(1, 11):
    T = int(input())
    arr = list(map(int, input().split()))
    i = 1
    while True:
        cycle(arr, i)
        i += 1
        if i > 5:
            i = 1
        if arr[len(arr) - 1] <= 0:
            arr[len(arr) - 1] = 0
            break
    print(f"#{T}", end=" ")
    print(*arr)