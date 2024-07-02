# 파일 명에 포함된 숫자를 반영한 정렬 기능을 구현
# 파일명 100글자 이내 / 영문 대소문자/ 숫자/ 공백/마침표/빼기
# 파일명 영어로 시작 / 숫자를 하나 이상 포함

# Head Number Tail
# foo   9   .txt    -> foo9.txt
# foo   010 bar020.zip  -> foo010bar020.zip

# Head부분을 기준으로 사전 순 정렬 / 대소문자 구분x
# 대소문자 차이 외에는 같을경우 -> Number 숫자 순으로 정렬 / 앞의 0은 무시
# Head 부분과 Number의 숫자도 같으면 원래 입력에 주어진 순서를 유지
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


# print(solution( ["img12.png", "img10.png", "img02.png", "img1.png", "IMG01.GIF", "img2.JPG"]))
# print(solution( ["F-5 Freedom Fighter", "B-50 Superfortress", "A-10 Thunderbolt II", "F-14 Tomcat"]))
print(solution(["foo9.txt", "foo010bar020.zip", "F-15"]))