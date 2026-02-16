import sys
input = sys.stdin.readline

N = int(input())
sizes = list(map(int, input().split()))
T, P = map(int, input().split())

tshirt_count = 0
for s in sizes:
    tshirt_count += (s + T - 1) // T

pen_bundle = N // P
pen_single = N % P

print(tshirt_count)
print(pen_bundle, pen_single)