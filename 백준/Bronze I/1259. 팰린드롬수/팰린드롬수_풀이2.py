while True:
    answer = 'yes'
    num = list(map(str, input()))
    if num[0] == '0':
        break
    for x in range(len(num) // 2):
        if num[x] != num[-x - 1]:
            answer = 'no'
            break
    print(answer)