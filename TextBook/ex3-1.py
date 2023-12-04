#카운터에는 거스름돈으로 사용할 500원, 100원, 50원, 10원짜리 동전이 무한히 존재한다고 가정
#손님에게 거슬러 줘야 할 돈이 N원일 때 거슬러줘야 할 동전의 최소 개수를 구하라

# change = int(input("거슬러 줘야 하는 금액을 입력하세요 : "))
#
# print(change//500)
# change = change % 500
# print(change//100)
# change = change % 100
# print(change//50)
# change = change % 50
# print(change//10)
# change = change % 10


change=1000-int(input())
count=0
coin_types=[500, 100, 50, 10, 5, 1]
for coin in coin_types:
    count+=change//coin
    change%=coin
print(count)