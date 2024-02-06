from collections import deque
N = int(input())
card_deque = deque([i for i in range(1, N + 1)])
while len(card_deque) != 1:
    card_deque.popleft()
    card_deque.rotate(-1)

print(card_deque[0])