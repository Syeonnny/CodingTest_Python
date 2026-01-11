from collections import deque

N = int(input())
queue = deque((i, x) for i, x in enumerate(map(int, input().split()), start=1))
ans = []

while queue:
    idx, value = queue.popleft()
    ans.append(idx)

    if not queue:
        break
        
    if value > 0:
        queue.rotate(-(value-1))
    else:
        queue.rotate(-value)

print(*ans)