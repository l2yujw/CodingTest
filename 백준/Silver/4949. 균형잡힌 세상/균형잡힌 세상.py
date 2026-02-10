import sys
input = sys.stdin.readline

while True:
    s = input().rstrip()
    if s == ".":
        break

    stack = []
    ok = True

    for c in s:
        if c == '(' or c == '[':
            stack.append(c)
        elif c == ')':
            if not stack or stack[-1] != '(':
                ok = False
                break
            stack.pop()
        elif c == ']':
            if not stack or stack[-1] != '[':
                ok = False
                break
            stack.pop()

    if ok and not stack:
        print("yes")
    else:
        print("no")
