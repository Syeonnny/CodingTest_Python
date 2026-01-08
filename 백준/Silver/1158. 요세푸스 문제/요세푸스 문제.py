from collections import deque

N, K = map(int, input().split())
queue = deque(range(1, N+1))

output = []
while queue:
    for _ in range(1, K):
        queue.append(queue.popleft())
    output.append(queue.popleft())

output = list(map(str, output))

print("<" + ", ".join(output) + ">")