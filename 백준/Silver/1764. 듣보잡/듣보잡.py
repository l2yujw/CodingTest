from sys import stdin
input = stdin.readline

N, M = map(int, input().split())

deud = set(input().rstrip() for _ in range(N))
mot = set(input().rstrip() for _ in range(M))

common = sorted(deud & mot)

print(len(common))
print('\n'.join(common))