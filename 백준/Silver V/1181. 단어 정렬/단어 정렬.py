from sys import stdin

input = stdin.readline
n = int(input())

words = [str(input().rstrip()) for i in range(n)]

words = list(set(words))
words.sort()
words.sort(key=len)

print('\n'.join(words))