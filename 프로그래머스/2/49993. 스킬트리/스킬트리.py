def solution(skill, skill_trees):
    answer = 0

    for i in skill_trees:
        temp = ''
        for j in i:
            if j in skill:
                temp += j

        if skill[:len(temp)] == temp:
            answer += 1

    return answer