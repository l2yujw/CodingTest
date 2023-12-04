cal = input()
temp = ''
k = 0
result = []
answer = 0
for i in range(len(cal)):
    if cal[i] == '+':
        k += int(temp)
        temp = ''
    elif cal[i] == '-':
        k += int(temp)
        result.append(k)
        k = 0
        temp = ''
    elif i == len(cal)-1:
        temp += str(cal[i])
        k += int(temp)
        result.append(k)
    else:
        temp += str(cal[i])

answer = result[0]

for k in range(1, len(result)):
    answer -= result[k]

print(answer)
