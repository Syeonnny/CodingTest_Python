from collections import deque

N, K = map(int, input().split())

MAX = 100000
dist = [-1] * (MAX + 1)   
ways = [0] * (MAX + 1)    

def bfs():
    queue = deque([N])
    dist[N] = 0
    ways[N] = 1

    while queue:
        x = queue.popleft()

        for nx in (x - 1, x + 1, x * 2):
            if 0 <= nx <= MAX:

                if dist[nx] == -1:
                    dist[nx] = dist[x] + 1
                    ways[nx] = ways[x]
                    queue.append(nx)

                elif dist[nx] == dist[x] + 1:
                    ways[nx] += ways[x]

bfs()
print(dist[K])
print(ways[K])