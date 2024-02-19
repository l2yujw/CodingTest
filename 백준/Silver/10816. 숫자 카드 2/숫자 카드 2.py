import sys
input=sys.stdin.readline

input()
cards={}
for i in input().split():
    if i in cards:
        cards[i]+=1
    else:
        cards[i]=1
input()
print(' '.join([str(cards[i]) if i in cards else '0' for i in input().split()]))