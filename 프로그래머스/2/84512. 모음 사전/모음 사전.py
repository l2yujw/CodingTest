def solution(word):
    answer = 0
    split = [i for i in word]
    arr = []
    alpha = ['A', 'E', 'I', 'O', 'U']
    while True:
        if arr == split or arr == ['U','U','U','U','U']:
            break

        if len(arr) < 5:
            arr.append('A')
            answer += 1
        else:
            while 'U' in arr:
                if arr[-1] == 'U':
                    arr.pop()
                else:
                    break
            arr.append(alpha[alpha.index(arr.pop()) + 1])
            answer += 1

    return answer