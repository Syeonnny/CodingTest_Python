from collections import deque

N, M = map(int, input().split())

jump = [0] * 101
dist = [-1] * 101

for _ in range(N+M):
    start, end = map(int, input().split())
    jump[start] = end

def bfs():
    dist[1] = 0 
    queue = deque([1])
    
    while queue:
        cur = queue.popleft()

        for d in range(1, 7):
            nxt = cur + d

            if nxt > 100:
                continue

            if jump[nxt] != 0:
                nxt = jump[nxt]

            if dist[nxt] == -1:
                dist[nxt] = dist[cur] + 1
                queue.append(nxt)

bfs()
print(dist[100])