a= 0.3 + 0.6
print(round(a, 4))

#소숫점 비교할땐 round를 써서 못잡는 오류를 신경써주자
if round(a,4) == 0.9:
    print(True)
else:
    print(False)

n = 10
a = [0] * n
print(a)

array = [i for i in range(10)]
print(array)

array = [i for i in range(20) if i % 2 == 1]
print(array)

array = [i*i for i in range(1, 10)]
print(array)

n = 4
m = 3
array = [[0] * m for _ in range(n)]
print(array)

# append #O(1) 리스트에 원소 삽입
# sort , sort(reverse = True)# O(NlogN) 오름차순, 내림차순
# reverse # O(N) 원소 순서 뒤집기
# insert # O(N) 특정한 위치에 원소를 삽입
# count # O(N) 데이터 개수 셈
# remove # O(N) 특정한 값을 갖는 원소를 모두 제거

#튜플은 키 값으로 사용하는 것이 좋음

#사전 자료형
data = dict()

data['사과'] = 'apple'
print(data)

b = {
    '홍길동' : 97,
    '이순신' : 98
}

print(b)

key_list = list(b.keys())
print(key_list)

# 집합 자료형 초기화 방법1
data = set([1, 2, 3])
print(data)

# 집합 자료형 초기화 방법2
data = {1, 1, 2, 3, 4, 4, 5}
print(data)

a = {1, 2, 3, 4, 5}
b = {3, 4, 5, 6, 7}

print(a | b) # 합집합
print(a & b) # 교집합
print(a - b) # 차집합


data = {1, 2, 3}
print(data)

data.add(4)
print(data)

data.update([5, 6])
print(data)


n = int(input())
data = list(map(int, input().split())) #map은 요소를 특정 데이터 타입으로 바꿈 split은 공백 기준 값 적용

print(n)
print(data)

import sys
# data = sys.stdin.readline().rstrip() #input보다 빠름
print(data)

answer = 7
print(f"정답은 {answer}입니다.")

#함수
a = 0

def fun():
    global a
    a += 1
    for i in range(10):
        fun()

print(a)

def operator(a, b):
    add_var = a + b
    subtract_var = a - b
    multiply_var = a * b
    return add_var, subtract_var, multiply_var

a, b, c = operator(7, 3)
print(a, b, c)

print((lambda a, b: a + b)(3, 7))

array2 = [('홍길동', 50), ('이순신', 32), ('아무개', 74)]

def my_key(x):
    return x[1]

print(sorted(array2, key=my_key))
print(sorted(array2, key=lambda x: x[1]))

# 실전에서 유용한 표준 라이브러리
# 내장함수 : 기본 입출력 함수부터 정렬 함수까지 김본적인 함수들을 제공
#     - 파이썬 프로그램을 작성할 때 없어서는 안 되는 필수적인 기능을 포합하고 있음
# itertools : 파이썬에서 반복되는 형태의 데이터를 처리하기 위한 유용한 기능들을 제공함
#     - 특히 순열과 조합 라이브러리는 코딩 테스트에서 자주 사용됩니다.
# heapq: 힙 자료구조를 제공합니다.
#     - 일반적으로 우선순위 큐 기능을 구현하기 위해 사용됩니다.
# bisect : 이진탐색 기능을 제공합니다.
# collections : 덱, 카운터 드으이 유요한 자료구조를 포함합니다.
# math : 필수적인 수학적 기능을 제공합니다.
#     - 팩토리얼, 제곱근, 최대공약수(GCD), 삼각함수 관련 함수부터 파이 같은 상수를 포함합니다.

from itertools import permutations
data2 = ['A', 'B', 'C']

result2 = list(permutations(data2, 3)) # 서로 다른 n개에서 서로 다른 r개를 선택하여 일렬로 나열하는 것
print(result2)

from itertools import combinations

result2 = list(combinations(data2, 2))
print(result2)

from itertools import product
result = list(product(data2, repeat=2)) # 두개를 뽑는 모든 순열 구하기 (중복허용)
print(result)

from itertools import combinations_with_replacement # 두개를 뽑는 모든 조합 구하기 (중복 허용)
result = list(combinations_with_replacement(data2, 2))
print(result)


from collections import Counter

counter = Counter(['red', 'blue', 'red', 'green', 'blue', 'blue'])

print(counter['blue']) # 'blue'가 등장한 횟수 출력
print(dict(counter)) # 사전 자료형으로 반환

import math

def lcm(a, b):
    return a * b // math.gcd(a, b)

a=21
b=14

print(math.gcd(21, 14))
print(lcm(21, 14))