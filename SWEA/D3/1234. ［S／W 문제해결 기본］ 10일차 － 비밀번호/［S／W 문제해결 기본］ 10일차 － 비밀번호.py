T = 10
for test_case in range(1, T + 1):
    N, password = input().split()
    ans = []

    for i in password:
        if not ans or ans[-1] != i:
            ans.append(i)
        else:
            ans.pop()

    a = ''.join(ans)
    print(f'#{test_case} {a}')
