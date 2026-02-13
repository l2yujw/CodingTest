from sys import stdin
input = stdin.readline

N = 1000 - int(input())
moneys = [500, 100, 50, 10, 5, 1]

answer = 0
for m in moneys:
    answer += N // m
    N = N % m

print(answer)