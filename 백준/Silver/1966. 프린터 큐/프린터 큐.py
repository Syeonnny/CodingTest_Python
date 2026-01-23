from collections import deque
T = int(input())

for i in range(T):
    N, M = map(int, input().split())

    lists = list(map(int, input().split()))
    cnt = 0 
    queue = deque((idx, v) for idx, v in enumerate(lists))

    while queue: 
        idx, v = queue.popleft()
        if any(v < pv for _, pv in queue):
            queue.append((idx, v))
        else: 
            cnt += 1 
            if idx == M:
                print(cnt)
                break