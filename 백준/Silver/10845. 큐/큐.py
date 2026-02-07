from collections import deque
from sys import stdin

def push(X):
    stack.append(X)

def pop():
    if len(stack) == 0:
        return -1
    return stack.popleft()

def size():
    return len(stack)

def empty():
    if len(stack) == 0:
        return 1
    return 0

def front():
    if len(stack) == 0:
        return -1
    return stack[0]

def back():
    if len(stack) == 0:
        return -1
    return stack[-1]

input = stdin.readline

N = int(input())
stack = deque()

for _ in range(N):
    command = list(input().split())

    if command[0] == 'push':
        push(command[1])
    elif command[0] == 'pop':
        print(pop())
    elif command[0] == 'size':
        print(size())
    elif command[0] == 'empty':
        print(empty())
    elif command[0] == 'front':
        print(front())
    elif command[0] == 'back':
        print(back())
