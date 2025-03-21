from collections import deque
def solution(priorities, location):
    queue = deque([(i,p) for i, p in enumerate(priorities)])
    print(queue)
    cnt = 0
    while queue:
        idx, value = queue.popleft()
        if any(p > value for _, p in queue):
            queue.append((idx,value))
        else:
            cnt += 1 
            if idx == location:
                return cnt
