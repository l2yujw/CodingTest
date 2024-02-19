import sys
input = sys.stdin.readline
N = int(sys.stdin.readline())
arr = []

def stack(process):
    command = process[0]
    if command == 'push':
        push(process)
    elif command == 'pop':
        pop()
    elif command == 'size':
        size()
    elif command == 'empty':
        empty()
    elif command == 'top':
        top()
    else:
        pass

def push(process):
    arr.append(process[1])

def pop():
    if len(arr) == 0:
        print(-1)
    else:
        print(arr.pop())

def size():
    print(len(arr))

def empty():
    if len(arr) == 0:
        print(1)
    else:
        print(0)

def top():
    if len(arr) > 0:
        print(arr[-1])
    else:
        print(-1)

for _ in range(N):
    command = sys.stdin.readline().split()
    stack(command)