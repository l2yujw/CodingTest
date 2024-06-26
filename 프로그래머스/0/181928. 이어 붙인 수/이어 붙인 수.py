def solution(num_list):
    answer = 0
    jjak = ''
    hol = ''
    for i in num_list:
        if i % 2 == 0:
            jjak += str(i)
        else:
            hol += str(i)
    return int(jjak) + int(hol)