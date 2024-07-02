def solution(files):
    answer = []

    # Head Number Tail 분리
    div = [[''] * 3 for _ in range(len(files))]
    posF = 0
    for file in files:
        temp = ''
        isChar = True
        posC = 0
        for c in file:
            if c.isdigit() and isChar:
                div[posF][0] = temp
                temp = c
                isChar = False
            else:
                if not c.isdigit() and not isChar:
                    div[posF][1] = temp
                    div[posF][2] = file[posC:]
                    break
                else:
                    temp += c

            if len(temp) != 0:
                div[posF][1] = temp
            posC += 1
        posF += 1

    print(div)
    #1번 & 2번 정렬
    div.sort(key=lambda x: (x[0].lower(), int(x[1])))

    for i in range(len(div)):
        temp = div[i][0] + div[i][1] + div[i][2]
        answer.append(temp)

    return answer