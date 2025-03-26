def solution(k, score):
    answer = []
    add = []
    for scores in score:
        add.append(scores)
        add.sort()
        if len(add)>k:
            add.pop(0)
        answer.append(min(add))
    return answer