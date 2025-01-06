
def separate(p):
    balance = 0
    for i, char in enumerate(p):
        balance = check_balance(balance, char)
        if balance == 0:
            return p[:i+1], p[i+1:]


def check_balance(balance, char):
    if char == '(':
        balance += 1
    else:
        balance -= 1
    return balance


def is_correct(p):
    balance = 0
    for char in p:
        balance = check_balance(balance, char)
        if balance < 0:
            return False
    return balance == 0


def solution(p):
    if not p:
        return ""

    u, v = separate(p)

    if is_correct(u):
        return u + solution(v)
    else:
        answer = '(' + solution(v) + ')'
        for char in u[1:-1]:
            if char == '(':
                answer += ')'
            else:
                answer += '('
        return answer