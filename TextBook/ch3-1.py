N = int(input())
count = 0

coinTypes = [500, 100, 50, 10]

for coin in coinTypes:
    count += N // coin
    N %= coin

print(count)