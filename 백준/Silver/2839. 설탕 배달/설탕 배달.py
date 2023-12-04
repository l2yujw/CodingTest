n = int(input())

p = n//5
temp = n

while n > 0:
    count = 0
    n = temp
    if p != 0:
        count += p
        n -= count * 5

    count += n // 3
    n %= 3

    if (n == 1 or n == 2) and p == 0:
        count = -1
        break
    elif n == 0:
        break
    else:
        p -= 1

print(count)