import copy

a= [1,2, [3,5], 4] # 복잡한 중첩 리스트인 경우
b= copy.deepcopy(a)
if a == b:
    print("true")

a=1
b=2
a, b = b, a
print(a, b)