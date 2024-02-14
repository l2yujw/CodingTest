N = int(input())
Nth = 666
count = 0

while True:
    if '666' in str(Nth):
        count += 1
    if count == N:
        print(Nth)
        break
    Nth += 1