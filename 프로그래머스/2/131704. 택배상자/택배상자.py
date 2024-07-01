def solution(order):
    stack = []
    n = len(order)
    idx = 0
    num = 0

    while idx < n:
        if order[idx] > num:
            num += 1
            stack.append(num)
        elif order[idx] == stack[-1]:
            stack.pop()
            idx += 1
        else:
            return idx

    return idx