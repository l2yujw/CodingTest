from collections import deque
def solution(cacheSize, cities):
    
    for i in range(0, len(cities)):
        cities[i] = cities[i].lower()
        
    answer = 0
    q = deque()
    
    if cacheSize == 0:
        return 5 * len(cities)
    
    for city in cities:
        if city in q:
            q.remove(city)
            q.append(city)
            answer += 1
        else:
            if len(q) >= cacheSize:
                q.popleft()
            q.append(city)
            answer += 5
    return answer