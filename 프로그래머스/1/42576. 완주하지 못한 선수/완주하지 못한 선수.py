from collections import Counter
def solution(participant, completion):
    participants = Counter(participant)
    completions = Counter(completion)
    p = participants - completions
    return list(p.keys())[0]