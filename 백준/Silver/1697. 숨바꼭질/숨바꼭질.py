from collections import deque

N, K = map(int,input().split())
Max = 10**6
visited = [False] * (Max+1)

def bfs(x):
    queue = deque()
    queue.append((x, 0)) 
    while queue:
        n, sec = queue.popleft()
        if n == K:
            return sec
        
        for nx in (n-1, n+1, n*2):
            if 0 <= nx <= Max and not visited[nx]:
                visited[nx] = True
                queue.append((nx, sec+1))

print(bfs(N))