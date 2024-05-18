def sol(index, flavor, kal):
    global max_flavor
    if kal > l:
        return
    if max_flavor < flavor:
        max_flavor = flavor
    if index == n:
        return

    f, k = kal_list[index]
    sol(index + 1, flavor + f, kal + k)
    sol(index + 1, flavor, kal)


T = int(input())
for test_case in range(1, T + 1):
    n, l = map(int, input().split())

    kal_list = [list(map(int, input().split())) for _ in range(n)]
    max_flavor = 0

    sol(0, 0, 0)
    print(f"#{test_case} {max_flavor}")