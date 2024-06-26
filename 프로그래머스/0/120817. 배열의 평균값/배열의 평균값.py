def solution(numbers):
    sum = 0
    length = 0
    for i in numbers:
        sum += i
        length += 1
    return sum / length