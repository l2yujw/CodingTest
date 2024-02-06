from collections import deque
deq = deque() # 덱 초기화

deq = deque([i for i in range(1, 5)])
deq.appendleft(10)
deq.append(-10)
print(deq.pop())
print(deq.popleft()) # 덱 길이
len(deq)
print(deq)
deq.rotate(-1) # 음수이면 왼쪽으로 회전


N = int(input())
card_deque = deque([i for i in range(1, N + 1)])
while len(card_deque) != 1:
    card_deque.popleft()
    card_deque.rotate(-1)

print(card_deque[0])