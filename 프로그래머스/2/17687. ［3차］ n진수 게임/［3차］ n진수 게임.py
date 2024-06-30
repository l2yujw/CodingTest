def solution(n, t, m, p):
    answer = ''
    num = 0
    pos = 0
    while True:
        if len(answer) >= t:
            break

        c = convert(num, n)
        for say in c:
            if pos % m == p - 1:
                answer += say
            pos += 1
        num += 1

    return answer[:t]

def convert(num, n):
    alphaNum = {10:'A', 11:'B', 12:'C', 13:'D', 14:'E', 15:'F'}

    c = ''
    if num == 0:
        return '0'

    if n > 10:
        while num > 0:
            temp = num % n
            if temp >= 10:
                c = str(alphaNum[num % n]) + c
            else:
                c = str(num % n) + c
            num //= n
    else:
        while num > 0:
            c = str(num % n) + c
            num //= n
    return c