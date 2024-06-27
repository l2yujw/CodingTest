def solution(num_list):
    a = 1
    for i in num_list:
        a *= i
    b = sum(num_list) ** 2
    if a < b:
        return 1
    else:
        return 0