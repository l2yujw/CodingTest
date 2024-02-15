while True:
    byun = list(map(int, input().split()))
    byun.sort()
    if byun[0] == 0 or byun[1] == 0 or byun[2] == 0:
        break
    if byun[0]**2 + byun[1]**2 == byun[2]**2:
        print("right")
    else:
        print("wrong")