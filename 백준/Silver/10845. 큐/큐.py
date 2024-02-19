from collections import deque
from sys import stdin
input = stdin.readline
N = int(stdin.readline())
arr = deque()

def queue(process):
    command = process[0]
    if command == 'push':
        push(process)
    elif command == 'pop':
        pop()
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

def push(process):
    arr.append(process[1])

def pop():
    if len(arr) == 0:
        print(-1)
    else:
        print(arr.popleft())

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
    command = input().split()
    queue(command)