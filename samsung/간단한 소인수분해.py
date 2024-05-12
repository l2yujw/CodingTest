N = int(input())

num = [2, 3, 5, 7, 11]
dic = {'a': 0, 'b': 0, 'c': 0, 'd': 0, 'e': 0}

i = 0

while N > 1:
    if N % num[i] == 0:
        N //= num[i]
        dic[chr(ord('a') + i)] += 1
    else:
        i += 1

print("#1", end=" ")
for value in dic.values():
    print(value, end=" ")