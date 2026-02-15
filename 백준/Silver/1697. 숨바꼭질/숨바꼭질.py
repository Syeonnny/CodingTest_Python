from collections import deque

N, K = map(int, input().split())
dist = [0] * 100001
visited = [False] * 100001 

if N == K:
    print(0)
    exit()

def bfs(x):
    visited[x] = True
    queue = deque([x])
    
    while queue: 
        x = queue.popleft()

        for nx in (x-1, x+1, 2*x):
            if 0 <= nx <= 100000 and not visited[nx]:
                visited[nx] = True
                queue.append(nx)
                dist[nx] = dist[x]+ 1
                if nx == K: 
                    return dist[nx]
        
print(bfs(N))