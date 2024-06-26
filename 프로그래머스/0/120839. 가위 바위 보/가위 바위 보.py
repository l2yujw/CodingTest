def solution(rsp):
    win = {'2': '0', '0': '5', '5': '2'}
    answer = ''
    for i in range(0, len(rsp)):
        answer += win[rsp[i]]
    return answer