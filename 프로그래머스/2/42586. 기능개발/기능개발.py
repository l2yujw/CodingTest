from collections import deque


def solution(progress, speeds):
    answer = []
    days = deque()

    for i in range(len(progress)):
        x = (100 - progress[i]) / speeds[i]

        if x == int(x):
            days.append(int(x))
        else:
            days.append(int(x) + 1)

    while days:
        temp = days.popleft()
        count = 1

        while days and temp >= days[0]:
            days.popleft()
            count += 1
        answer.append(count)

    return answer