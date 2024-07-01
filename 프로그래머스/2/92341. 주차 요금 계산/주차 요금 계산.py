import math
def solution(fees, records):
    answer = []
    cars = {}
    answer = {}
    for i in records:
        split = i.split()
        if split[2] == 'IN':
            cars[split[1]] = split[0]
        else:
            inTime = cars.get(split[1]).split(":")
            outTime = split[0].split(":")
            minute = (int(outTime[0]) - int(inTime[0])) * 60 + (int(outTime[1]) - int(inTime[1]))
            if split[1] in answer.keys():
                answer[split[1]] += minute
            else:
                answer[split[1]] = minute
            pop = cars.pop(split[1])

    for i in cars:
        inTime = cars.get(i).split(":")
        minute = (23 - int(inTime[0])) * 60 + (59 - int(inTime[1]))
        if i in answer.keys():
            answer[i] += minute
        else:
            answer[i] = minute

    for i in answer:
        if answer[i] <= fees[0]:
            answer[i] = fees[1]
        else:
            answer[i] = fees[1] + math.ceil((answer[i] - fees[0]) / fees[2]) * fees[3]

    d = sorted(answer)
    ans = []
    for i in d:
        ans.append(answer[i])

    return ans