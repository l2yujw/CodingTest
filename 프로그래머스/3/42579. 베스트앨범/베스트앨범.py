# 장르별 가장 많이 재생된 노래 두개씩 묶음
# 1. 속한 노래가 많이 재생된 장르
# 2. 장르 내에서 가장 많이 재생된
# 3. 장르내에서 재생 같 => 고유번호 낮은
# genres: 장르, plays: 노래별 재생 횟수
# 고유번호 순서대로 return
# genres[i] 고유번호 i, play[i] 재생횟수 i
# 가장 횟수많 장르 많부터 2개, 순차적으로 진행

def solution(genres, plays):
    answer = []
    dic = {}
    dic_total = {}
    for i, (genre, play) in enumerate(zip(genres, plays)):
        if genre not in dic:
            dic[genre] = [(i, play)]
        else:
            dic[genre].append((i, play))
            
        if genre not in dic_total:
            dic_total[genre] = play
        else:
            dic_total[genre] += play
            
    for (k, v) in sorted(dic_total.items(), key = lambda x: x[1], reverse = True):
        for (i, p) in sorted(dic[k], key = lambda x: x[1], reverse = True)[:2]:
            answer.append(i)
    
    return answer