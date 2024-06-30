def solution(n, k):
    answer = 0

    jinsoo = ''
    while n > 0:
        jinsoo = str(n % k) + jinsoo
        n //= k

    jinsoo = jinsoo.split("0")
    print(jinsoo)

    for i in jinsoo:
        if len(i) == 0:
            continue
        if int(i) < 2:
            continue
        
        if isPrime(int(i)):
            answer += 1

    return answer


def isPrime(num):
    if num == 1:
        return False
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            return False
    return True