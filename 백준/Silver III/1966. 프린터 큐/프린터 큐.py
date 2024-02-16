from collections import deque

num = int(input())
for i in range(num):
    cnt = 0
    N, M = map(int, input().split())
    imp = deque(list(map(int, input().split())))

    while len(imp) > 0:
        maxi = max(imp)
        if imp[0] == maxi:
            imp.popleft()
            if M == 0:
                cnt += 1
                break
            else:
                cnt += 1
                M -= 1
        else:
            a = imp.popleft()
            imp.append(a)
            if M == 0:
                M += len(imp) - 1 
            else:
                M -= 1
    print(cnt)