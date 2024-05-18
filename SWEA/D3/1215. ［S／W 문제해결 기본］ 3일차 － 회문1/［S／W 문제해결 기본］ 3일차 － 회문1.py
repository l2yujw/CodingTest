for test_case in range(1, 11):
    n = int(input())
    arr = [list(map(str, input())) for _ in range(8)]
    arrZ = list(map(list, zip(*arr)))

    count = 0
    for i in range(8):
        for k in range(8 - n + 1):
            s = arr[i][k:k+n]
            sZ = arrZ[i][k:k+n]
            if s == s[::-1]:
                count += 1
            if sZ == sZ[::-1]:
                count += 1

    print(f"#{test_case} {count}")