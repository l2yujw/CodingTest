from sys import stdin
input = stdin.readline

T = int(input())
for t in range(T):
    H, W, N = map(int, input().split())

    print(((N-1)%H+1)*100+((N-1)//H+1))