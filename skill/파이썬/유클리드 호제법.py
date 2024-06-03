def gcd(a, b):
    if b == 0: return a
    else: return gcd(b, a%b)

# main
n = int(input())
for _ in range(n):
    a, b= map(int, input().split())

    GCD = gcd(a,b) #최대공약수
    LCM = int(a*b/GCD) #최소공배수
    print(LCM,GCD)