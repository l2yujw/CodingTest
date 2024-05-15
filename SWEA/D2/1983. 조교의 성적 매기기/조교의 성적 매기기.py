dic = {0: 'A+', 1: 'A0', 2: 'A-', 3: 'B+', 4: 'B0', 5: 'B-', 6: 'C+', 7: 'C0', 8: 'C-', 9: "D0"}

T = int(input())
for test_case in range(1, T + 1):
    n, k = map(int, input().split())

    result = []
    for i in range(n):
        m, f, h = map(int, input().split())
        result.append([((35 * m) + (45 * f) + (20 * h)), i])

    result.sort(reverse=True)

    count = 0
    for x in result:
        if x[1] == (k - 1):
            print(f"#{test_case} {dic[count // (n // 10)]}")
            break
        count += 1