T = int(input())
for test_case in range(1, T + 1):
    n = int(input())
    maze = [list(map(int, input().split())) for _ in range(n)]

    turn_90 = list(map(list, zip(*maze[::-1])))
    turn_180 = list(map(list, zip(*turn_90[::-1])))
    turn_270 = list(map(list, zip(*turn_180[::-1])))

    print("#%d" % test_case)
    for i in range(len(maze)):
        print("".join(map(str, turn_90[i])), end=" ")
        print("".join(map(str, turn_180[i])), end=" ")
        print("".join(map(str, turn_270[i])), end="\n")