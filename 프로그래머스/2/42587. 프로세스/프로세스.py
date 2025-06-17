from collections import deque
def solution(priorities, location):
    answer = 0
    priorities = deque([(i,p) for i,p in enumerate(priorities)])
    while priorities:
        current = priorities.popleft()
        if any(current[1] < p[1] for p in priorities):
            priorities.append(current)
        else:
            answer += 1
            if location == current[0]:
                return answer