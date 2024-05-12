T = int(input())
for test_case in range(1, T + 1):
    day = [0, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

    arr = list(map(int, input().split()))

    res = 1
    for i in range(arr[0], arr[2]):
        res += day[i]

    res = res - arr[1] + arr[3]
    print("#%d %d" %(test_case, res))