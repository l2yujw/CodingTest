cal = list(input())

stack = []
answer = 0
tmp = 1

for i in range(len(cal)):
    if cal[i] == '(':
        stack.append(cal[i])
        tmp *= 2
    elif cal[i] == '[':
        stack.append(cal[i])
        tmp *= 3
    elif cal[i] == ')':
        if not stack or stack[-1] == '[':
            answer = 0
            break
        if cal[i-1] == '(':
            answer += tmp
        stack.pop()
        tmp //= 2
    elif cal[i] == ']':
        if not stack or stack[-1] == '(':
            answer = 0
            break
        if cal[i-1] == '[':
            answer += tmp
        stack.pop()
        tmp //= 3
    else:
        print("오류")

if stack:
    print(0)
else:
    print(answer)