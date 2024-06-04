#m n 보다 작은 x y
#첫해 1:1 둘 2:2 x:y 다음의 해를 표현 x':y'
#if x < m 이면 x' = x + 1 else x = 1
#if y < n 이면 y' = Y + 1 else y = 1
#m:n 은 마지막 해
#m =10 n = 12, 첫 1:1 11번째 1:11 3:1은 13번째 10:12는 마지막 60번째 즉 최소 공배수네

def gcd(n, m):
    while m > 0:
        n, m = m, n % m
    return n


def lcm(n, m):
    return n // gcd(n, m) * m


t = int(input())
for _ in range(t):
    m, n, x, y = map(int, input().split())
    check = x
    while check <= lcm(m, n):
        num = check % n
        if num == 0:
            num = n
        if num == y:
            print(check)
            break
        check += m
    else:
        print(-1)