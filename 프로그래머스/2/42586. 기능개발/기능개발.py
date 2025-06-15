from math import ceil

def solution(progresses, speeds):
    answer = []
    new = []
    count = 0
    for i in range(len(progresses)):
        answer.append(ceil((100-progresses[i])/speeds[i]))
    tmp = answer[0]
    for i in range(len(answer)):
        if answer[i] <= tmp:
            count += 1
        else:
            new.append(count)
            count = 1
            tmp = answer[i]
    new.append(count)
    return new