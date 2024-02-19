from collections import deque
from sys import stdin
input = stdin.readline
N = int(stdin.readline())
arr = deque()

def dequeFunc(process):
    command = process[0]
    if command == 'push_front':
        push(command, process[1])
    elif command == 'push_back':
        push(command, process[1])
    elif command == 'pop_front':
        pop(command)
    elif command == 'pop_back':
        pop(command)
    elif command == 'size':
        size()
    elif command == 'empty':
        empty()
    elif command == 'front':
        front()
    elif command == 'back':
        back()
    else:
        pass

def push(command, X):
    if command == 'push_front':
        arr.appendleft(X)
    else:
        arr.append(X)

def pop(command):
    if len(arr) == 0:
        print(-1)
    elif command == 'pop_front':
        print(arr.popleft())
    else:
        print(arr.pop())

def size():
    print(len(arr))

def empty():
    if len(arr) == 0:
        print(1)
    else:
        print(0)

def front():
    if len(arr) > 0:
        print(arr[0])
    else:
        print(-1)

def back():
    if len(arr) > 0:
        print(arr[-1])
    else:
        print(-1)

for _ in range(N):
    command = input().rstrip().split()
    dequeFunc(command)