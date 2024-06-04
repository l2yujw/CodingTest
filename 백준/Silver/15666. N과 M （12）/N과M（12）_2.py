A, B = map(int,input().split())
i = 1

while A < B:
    if B % 10 == 1: B //= 10
    elif not B % 2: B //= 2
    else: B = 0
    i += 1
print(-1 if A > B else i)