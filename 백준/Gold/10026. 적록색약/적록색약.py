from collections import deque

N = int(input())
colors = [list(input().strip()) for _ in range(N)]

dx = [0, 0, -1, 1]
dy = [-1, 1, 0, 0]

no_visited = [[False]*N for _ in range(N)]
weak_visited = [[False]*N for _ in range(N)]

no_cnt = 0 
weak_cnt = 0

def bfs(x, y, visited, weak=False):
    queue = deque([(x,y)])
    visited[x][y] = True

    while queue:
        x, y = queue.popleft()
        cur = colors[x][y]
        
        for d in range(4):
            nx = x + dx[d]
            ny = y + dy[d]

            if 0 <= nx < N and 0 <= ny < N and not visited[nx][ny]:
                nxt = colors[nx][ny]

                if not weak:
                    if nxt == cur: 
                        visited[nx][ny] = True
                        queue.append((nx, ny))
                else:
                    if (cur == 'B' and nxt == 'B') or (cur in ('R', 'G') and nxt in ('R', 'G')):
                        visited[nx][ny] = True
                        queue.append((nx, ny))


for i in range(N):
    for j in range(N):
        if not no_visited[i][j]: 
            bfs(i,j, no_visited)
            no_cnt += 1
            
for i in range(N):
    for j in range(N):
        if not weak_visited[i][j]:
            bfs(i, j, weak_visited, weak=True)
            weak_cnt += 1

print(no_cnt, weak_cnt)