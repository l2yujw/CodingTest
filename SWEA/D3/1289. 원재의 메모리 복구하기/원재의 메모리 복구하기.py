T = int(input())
for test_case in range(1, T + 1):
    n = input().rstrip()

    num = '1'

    count = 0
    for i in n:
        if i == num:
            count += 1
            if num == '1':
                num = '0'
            else:
                num = '1'

    print(f"#{test_case} {count}")