def solution(str1, str2):
    str1 = str1.lower()
    str2 = str2.lower()
    left = []
    right = []
    for i in range(0, len(str1) - 1):
        if str1[i].isalpha() and str1[i + 1].isalpha():
            left.append([str1[i] + str1[i + 1]])

            
    for i in range(0, len(str2) - 1):
        if str2[i].isalpha() and str2[i + 1].isalpha():
            right.append([str2[i] + str2[i + 1]])

    if len(left) == 0 and len(right) == 0:
        return 1 * 65536

    tot = len(left) + len(right)
    cross = 0
    if len(left) > len(right):
        for v in right:
            if v in left:
                left.remove(v)
                cross += 1
    else:
        for v in right:
            if v in left:
                left.remove(v)
                cross += 1

    tot -= cross

    J = int((cross / tot) * 65536)

    return J