nineShorts = []
sevenShorts = []

for i in range(9):
    nineShorts.append(int(input()))

val = sum(nineShorts) - 100

for a in range(9):
    for b in range(a + 1, 9):
        if nineShorts[a] + nineShorts[b] == val:
            x = nineShorts[a]
            y = nineShorts[b]

nineShorts.remove(x)
nineShorts.remove(y)
nineShorts.sort()

for i in nineShorts:
    print(i)