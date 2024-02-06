n = int(input())
list_a = sorted(map(int,input().split(' ')))
list_b = list(map(int,input().split(' ')))

sum = 0
for a in list_a:
    mb = max(list_b)
    sum += a*mb
    list_b.remove(mb)
print(sum)