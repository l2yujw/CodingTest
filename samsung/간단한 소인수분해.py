T = int(input())
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):
    N = int(input())

    num = [2, 3, 5, 7, 11]
    dic = {'a': 0, 'b': 0, 'c': 0, 'd': 0, 'e': 0}

    i = 0

    while N > 1:
        if N % num[i] == 0:
            N //= num[i]
            dic[chr(ord('a') + i)] += 1
        else:
            i += 1

    print("#%d" %(test_case), end=" ")
    for value in dic.values():
        print(value, end=" ")
    print()