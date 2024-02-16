from sys import stdin

def isPrime(num):
    if num == 1:
        return False
    elif num == 2 or num == 3:
        return True
    elif num % 2 == 0 or num % 3 == 0:
        return False
    else:
        for x in range(2, int(num**0.5)+1):
            if num%x == 0:
                return False
        return True

input = stdin.readline
M, N = map(int, input().split())

for x in range(M, N + 1):
    if isPrime(x):
        print(x)