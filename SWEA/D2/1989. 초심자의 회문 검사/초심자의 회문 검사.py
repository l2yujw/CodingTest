T = int(input())
for test_case in range(1, T + 1):
    word = input().rstrip()
    r = word[::-1]
    if word == r:
        print("#%d 1" % (test_case))
    else:
        print("#%d 0" % (test_case))