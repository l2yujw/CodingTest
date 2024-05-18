T = 10
for test_case in range(1, T + 1):
    n = int(input())
    arr = [list(map(str, input())) for _ in range(100)]
    arrZ = list(map(list, zip(*arr)))

    count = 0
    for i in range(100):
        for k in range(100):
            for x in range(k + 1, 101):
                s = arr[i][k:x]
                sZ = arrZ[i][k:x]
                if s == s[::-1]:
                    if len(s) > count:
                        count = len(s)
                if sZ == sZ[::-1]:
                    if len(sZ) > count:
                        count = len(sZ)

    print(f"#{n} {count}")