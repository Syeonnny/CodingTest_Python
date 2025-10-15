from collections import deque
def solution(priorities, location):
    rank = 0
    queue = deque([(idx, p) for idx, p in enumerate(priorities)])
    while queue:
        idx, prior = queue.popleft()
        if any(p > prior for _, p in queue):
            queue.append((idx,prior))
        else:
            rank += 1
            if idx == location:
                return rank