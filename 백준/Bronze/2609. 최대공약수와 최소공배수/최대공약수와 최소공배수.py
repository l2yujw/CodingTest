def gcd(a, b):
    if b == 0:
        return a
    else:
        return gcd(b, a % b)


m, n = map(int, input().split(" "))
print(gcd(m, n),int(m*n/gcd(m,n)),sep="\n")