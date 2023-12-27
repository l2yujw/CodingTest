N, K = map(int, input().split())

count = 1

while count <= N:
    if N % count == 0:
        K -= 1
    if K == 0:
        print(count)
        break

    count += 1

if K != 0:
    print(0)