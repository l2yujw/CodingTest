arr = []
for _ in range(int(input())):
    arr.append(list(map(int, input().split())))

#key=lamda x: (x[0], x[1]) x[0]을 기준으로 오름차순 같으면 x[1]기준으로 오름차순
#만약 -x[] 형식이면 내림차순임
arr.sort(key=lambda x: (x[0], x[1]))

for e in arr:
    print(str(e[0]) + " " + str(e[1]))

a=1
b=2
res = a if a > b else b