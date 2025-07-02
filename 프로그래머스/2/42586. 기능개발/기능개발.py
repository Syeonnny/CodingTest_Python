from math import ceil 
from collections import deque

def solution(progresses, speeds):
    answer = []
    work = deque()
    
    for i in range(len(progresses)):
        working = ceil((100-progresses[i])/speeds[i])
        work.append(working)
    while work:
        curr = work.popleft()
        count = 1
        while work and work[0] <= curr:
            work.popleft()
            count +=1 
        answer.append(count)
    return answer