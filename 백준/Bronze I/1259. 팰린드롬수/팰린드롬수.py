import sys
input=sys.stdin.readline

while True:
    txt=input().strip()
    if txt=="0":break
    if txt==txt[::-1]:print("yes")
    else:print("no")