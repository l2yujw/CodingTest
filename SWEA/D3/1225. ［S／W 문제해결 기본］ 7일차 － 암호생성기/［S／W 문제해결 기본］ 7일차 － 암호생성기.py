def cycle(arr):
    for x in range(1, 6):
        arr.append(arr.pop(0) - x)
        if arr[len(arr) - 1] <= 0:
            arr[len(arr) - 1] = 0
            break


for test_case in range(1, 11):
    T = int(input())
    arr = list(map(int, input().split()))
    while True:
        cycle(arr)
        if arr[len(arr) - 1] == 0:
            break

    print(f"#{T}", end=" ")
    print(*arr)