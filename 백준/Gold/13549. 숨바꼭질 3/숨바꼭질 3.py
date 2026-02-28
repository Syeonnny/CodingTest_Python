from collections import deque

N, K = map(int, input().split())
MAX = 100000
INF = 10**9

dist = [INF] * (MAX + 1)
queue = deque([N])
dist[N] = 0

while queue:
    x = queue.popleft()
    if x == K:
        break

    nx = x * 2
    if 0 <= nx <= MAX and dist[nx] > dist[x]:
        dist[nx] = dist[x]
        queue.appendleft(nx)

    nx = x - 1
    if 0 <= nx <= MAX and dist[nx] > dist[x] + 1:
        dist[nx] = dist[x] + 1
        queue.append(nx)

    nx = x + 1
    if 0 <= nx <= MAX and dist[nx] > dist[x] + 1:
        dist[nx] = dist[x] + 1
        queue.append(nx)

print(dist[K])