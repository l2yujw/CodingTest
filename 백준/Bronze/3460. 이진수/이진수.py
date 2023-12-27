T = int(input())

for i in range(T):
    n = int(input())
    count = 0

    while n > 0:
        if n % 2 == 1:
            print(count, end=" ")
        n //= 2
        count += 1
    print()