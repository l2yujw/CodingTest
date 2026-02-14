import heapq
import sys
input = sys.stdin.readline

N = int(input())
cards = []

for _ in range(N):
    heapq.heappush(cards, int(input()))

answer = 0

while len(cards) > 1:
    a = heapq.heappop(cards)
    b = heapq.heappop(cards)
    cost = a + b
    answer += cost
    heapq.heappush(cards, cost)

print(answer)