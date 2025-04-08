# 판매 수익 얻음
# 자신이 참여시킨 추천인에게서 발생하는 10%까지 자신의 이익
# 마찬가지로 자신을 추천해준 사람에게 발생하는 이익의 10%감
# 10% 계산 금액이 1원미만이면 자신이 가짐

# enroll: 판매원 이름, referral: 추천인 이름 (enroll i번째에 있는 판매원의)
# seller: 판매한 사람, amount: 판매량(seller i번째에 있는 판매원의)
# 칫솔 한 개 이익 100원 고정

# enroll dict 이름, i for문
# graph 0~len[enroll]
# referral graph[dict[referral[i]]].append(i)
# dfs 타고 들어가다가 dict[seller[i]] == 현재 판매원 i
# 지금까지 방문한 visited의 i번째 결과에 10%씩해서 더하기
# 조건 방문해제 필요
# dfs(x) 환경
# for i in graph[x] 방문처리 if seller 조건: 결과합,
# dfs(i) 방문처리 해제
def solution(enroll, referral, seller, amount):
    name_to_idx = {name: i for i, name in enumerate(enroll)}
    result = [0] * len(enroll)

    ref_map = {}
    for i, name in enumerate(enroll):
        ref_map[name] = referral[i]

    def dfs(person, money):
        if person == "-" or money < 1:
            return
        idx = name_to_idx[person]
        give = money // 10
        result[idx] += money - give
        dfs(ref_map[person], give)

    for i in range(len(seller)):
        dfs(seller[i], amount[i] * 100)

    return result
