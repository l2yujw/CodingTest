# 장르별 가장 많이 재생된 노래 (두 개씩)
# 고유 번호 구분
# 1. 장르별, 2. 장르 내부, 2-1. 같으면 고유번호 낮은 노래 우선

# genres: 장르, plays: 재생 횟수
# return 베스트 앨범에 들어갈 노래의 고유번호 순서대로

# genres[i]: 고유번호 i
# plays[i]: 고유번호 i
# 장르에 속한게 하나 -> 한곡만 선택

def solution(genres, plays):
    songs = list(enumerate(zip(genres, plays)))
    songs.sort(key = lambda x:(-x[1][1], x[0]))
    
    best = {}
    best_genre = {}
    for i, (genre, play) in songs:
        if genre not in best_genre:
            best_genre[genre] = play
        else:
            best_genre[genre] += play
            
    sorted_genres = sorted(best_genre.items(), key = lambda x:-x[1])
    
    answer = []
    
    for genre, _ in sorted_genres:
        count = 0
        for i, (g, _) in songs:
            if g == genre:
                answer.append(i)
                count += 1
                if count == 2:
                    break
                    
    return answer