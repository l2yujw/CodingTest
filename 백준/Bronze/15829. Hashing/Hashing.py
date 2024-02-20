import sys
input=sys.stdin.readline
L = int(input())
user_input = input()
Mod = 1234567891
r = 31

answer = 0

for i in range(L):
    num = ord(user_input[i]) - 96
    answer += num * (r ** i)

print(answer % Mod)