def solution(a, b):
    left = int(str(a) + str(b))
    right = 2 * a * b
    if left > right:
        return left
    else:
        return right
