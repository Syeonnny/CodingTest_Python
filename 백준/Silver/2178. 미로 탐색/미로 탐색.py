from collections import deque
N, M = map(int, input().split())

graph = [list(map(int, input().strip())) for _ in range(N)]

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]


dist = [[0]*M for _ in range(N)]

def bfs(x, y):
    queue = deque() 
    queue.append((x,y))
    dist[x][y] = 1 

    while queue:
        x, y = queue.popleft()

        for d in range(4):
            nx = x + dx[d]
            ny = y + dy[d]

            if nx < 0 or ny < 0 or nx >= N or ny >= M:
                continue
        
            if graph[nx][ny] == 1 and dist[nx][ny] == 0:
                queue.append((nx, ny))           
                dist[nx][ny] = dist[x][y] + 1

    return dist[N-1][M-1]

print(bfs(0,0))