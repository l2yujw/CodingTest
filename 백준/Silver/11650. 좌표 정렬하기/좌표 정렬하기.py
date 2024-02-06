arr = []
for _ in range(int(input())):
    arr.append(list(map(int, input().split())))

arr.sort(key=lambda x: (x[0], x[1]))

for e in arr:
    print(str(e[0]) + " " + str(e[1]))