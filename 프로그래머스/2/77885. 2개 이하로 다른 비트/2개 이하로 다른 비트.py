def solution(numbers):
    answer = []

    for number in numbers:
        binNum = list('0' + bin(number)[2:])
        idx = ''.join(binNum).rfind('0')
        binNum[idx] = '1'

        if number % 2 == 1:
            binNum[idx + 1] = '0'
        
        answer.append(int(''.join(binNum), 2))

    return answer