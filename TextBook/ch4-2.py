n = int(input())
count = 0

for hour in range(n + 1):
    if hour % 10 == 3 or hour // 10 == 3:
        count += 60*60
        continue
    for min in range(60):
        if min % 10 == 3 or min // 10 == 3:
            count += 60
            continue
        for sec in range(60):
            if sec % 10 == 3 or sec // 10 == 3:
                count += 1

print(count)

count = 0
for i in range(h + 1):
    for j in  range(60):
        for k in range(60):
            if '3' in str(i) + str(j) + str(k):
                count += 1

print(count)