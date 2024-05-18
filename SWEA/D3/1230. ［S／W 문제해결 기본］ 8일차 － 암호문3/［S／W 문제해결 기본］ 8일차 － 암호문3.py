inst_list = ['I', 'D', 'A']
for test_case in range(1, 11):
    n = int(input())
    origin = list(map(int, input().split()))
    m = int(input())
    inst = list(input().split())

    type = ''
    pos = -1
    cnt = -1
    for i in range(len(inst)):
        if inst[i] in inst_list :
            type = inst[i]
            pos = -1
            cnt = -1
        else:
            if type == "I":
                if pos == -1:
                    pos = int(inst[i])
                    continue
                else:
                    if cnt == -1:
                        cnt = int(inst[i])
                        continue

                    origin.insert(pos, inst[i])
                    pos += 1
            if type == "D":
                if pos == -1:
                    pos = int(inst[i])
                    continue
                else:
                    if cnt == -1:
                        cnt = int(inst[i])
                    for x in range(cnt):
                        origin.remove(origin[pos + x])
            if type == "A":
                if pos == -1:
                    pos = int(inst[i])
                    continue
                else:
                    if cnt == -1:
                        cnt = int(inst[i])
                        continue

                    origin.append(inst[i])
                    pos += 1

    print(f"#{test_case}", end=' ')
    print(*origin[:10])