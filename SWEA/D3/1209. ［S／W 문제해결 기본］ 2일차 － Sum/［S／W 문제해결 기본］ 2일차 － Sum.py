for test_case in range(10):
    T = int(input())
    arr = [list(map(int, input().split())) for _ in range(100)]
    arrZ = list(map(list, zip(*arr)))
    ans = []
    m ,r, l = 0, 0, 0
    for y in range(len((arr))):
        ans.append(sum(arr[y]))
        ans.append(sum(arrZ[y]))
        r += arr[y][y]
        l += arr[len(arr) - 1 - y][y]

    ans.append(r)
    ans.append(l)
    print(f"#{T} {max(ans)}")