N = int(input())
P = list(map(int, input().split()))

# 번호를 앞에 묶어서 list화
people = [(i + 1, P[i]) for i in range(N)]
# 번호는 그대로 두고 실질적인 값을 기준으로 정렬
people.sort(key=lambda x: x[1])
# 정렬 후에도 순서가 남을 수 있게 됌
# ex) [(1, 3)(2, 1)(3, 4)] -> [(2, 1)(1, 3)(3, 4)]

answer = 0
current = 0
order = []

for person, time in people:
    current += time
    answer += current
    order.append(person)

print(answer)
print(*order)
