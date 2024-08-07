def solution(record):
    answer = []
    dic = {}
    
    for r in record:
        r_split = r.split()
        if len(r_split) == 3:
            dic[r_split[1]] = r_split[2]
        
    for r in record:
        r_split = r.split()
        if r_split[0] == 'Enter':
            answer.append('%s님이 들어왔습니다.' %(dic[r_split[1]]))
        elif r_split[0] == 'Leave':
            answer.append('%s님이 나갔습니다.' %(dic[r_split[1]]))
                                              
    return answer