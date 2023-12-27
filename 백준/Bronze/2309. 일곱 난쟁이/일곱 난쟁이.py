nineShorts = []
sevenShorts = []
sumH = 0
exceptNum1, exceptNum2 = 0, 1

for i in range(9):
    nineShorts.append(int(input()))

while True:
    sumH = sum(nineShorts) - (nineShorts[exceptNum1] + nineShorts[exceptNum2])
    if sumH == 100:
        for i in range(9):
            if i == exceptNum1:
                continue
            elif i == exceptNum2:
                continue
            else:
                sevenShorts.append(nineShorts[i])
        break

    if exceptNum2 == 8:
        exceptNum1 += 1
        exceptNum2 = exceptNum1 + 1
    else:
        exceptNum2 += 1

sevenShorts.sort()
for i in range(7):
    print(sevenShorts[i])