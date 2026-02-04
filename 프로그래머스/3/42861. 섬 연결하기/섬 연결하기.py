def solution(n, costs):
    # 간선 비용 기준 정렬
    costs.sort(key=lambda x: x[2])
    
    # 부모 테이블 초기화
    parent = [i for i in range(n)]
    
    def find(x):
        if parent[x] != x:
            parent[x] = find(parent[x])  # 경로 압축
        return parent[x]
    
    def union(a, b):
        root_a = find(a)
        root_b = find(b)
        if root_a != root_b:
            parent[root_b] = root_a
            return True
        return False

    answer = 0
    for a, b, cost in costs:
        if union(a, b):  # 사이클이 아니라면 연결
            answer += cost
            
    return answer
