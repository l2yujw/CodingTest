# 추천인으로 부터 받은 10%까지 포함해서 위로 10% 제공

# enroll: 판매원 이름, referral: 자기를 참여시킨 판매원
# seller, amount: 사람, 판매량

# "-" center직할
# amount * 100 보장

def solution(enroll, referral, seller, amount):
    enroll_idx = {name: i for i, name in enumerate(enroll)}
    result = [0] * len(enroll)
    
    parent = [-1] * len(enroll)
    for i in range(len(referral)):
        if referral[i] != '-':
            parent[i] = enroll_idx[referral[i]]
        
    for i in range(len(seller)):
        dfs(parent, enroll_idx[seller[i]], amount[i] * 100, result)
    
    return result
        
        
def dfs(parent, idx, money, result):
    if idx == -1 or money < 1:
        return
    give = money // 10
    get = money - give
    result[idx] += get
    dfs(parent, parent[idx], give, result)