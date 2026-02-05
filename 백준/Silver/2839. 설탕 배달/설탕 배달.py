n = int(input())

five = n // 5

while five >= 0:
    if (n - (five * 5)) % 3 == 0:
        break
    five -= 1

if five >= 0:
    print(five + (n - (five * 5)) // 3)
else:
    print(-1)