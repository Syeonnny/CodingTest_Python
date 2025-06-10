from itertools import combinations
def solution(numbers):
    answer = []
    nCr = list(combinations(numbers,2))
    for i in nCr:
        answer.append(i[0]+i[1])
    return sorted(set(answer))