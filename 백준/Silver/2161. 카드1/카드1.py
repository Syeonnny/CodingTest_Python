N = int(input())

from collections import deque

queue = deque(range(1, N+1))
discards = []

while len(queue) > 1:
    discards.append(queue.popleft())
    queue.append(queue.popleft())

discards.append(queue[0])

print(*discards)