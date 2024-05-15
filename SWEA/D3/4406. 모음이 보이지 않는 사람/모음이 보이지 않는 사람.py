mask = ['a', 'e', 'i', 'o', 'u']
for test_case in range(int(input())):
    print(f"#{test_case + 1}", end=" ")
    en = input().rstrip()
    for i in en:
        if i in mask:
            continue
        else:
            print(i, end="")
    print()