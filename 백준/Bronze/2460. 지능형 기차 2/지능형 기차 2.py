STOP = 10

outPerson, inPerson = 0, 0
maxPerson, currentPerson = 0, 0
for i in range(STOP):
    outPerson, inPerson = map(int, input().split())
    currentPerson += (inPerson - outPerson)
    maxPerson = max(maxPerson, currentPerson)

print(maxPerson)