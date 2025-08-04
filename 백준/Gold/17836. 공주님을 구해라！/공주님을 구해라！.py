from collections import deque
n, m, t = map(int, input().split())

graph = [list(map(int, input().split())) for _ in range(n)]

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

queue = deque()
visited = [[False]*m for _ in range(n)]
visited[0][0] = True
queue.append((0,0))

min_distance = float('inf')
gram_distance = float('inf')

def bfs():
    global gram_distance
    dist = [[-1]*m for _ in range(n)]
    dist[0][0] = 0
    
    while queue:
        x, y = queue.popleft()
        
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            
            if not (0 <= nx < n and 0 <= ny < m):
                continue
            if visited[nx][ny] or graph[nx][ny]==1:
                continue
                
            visited[nx][ny] = True
            dist[nx][ny] = dist[x][y]+1
            queue.append((nx, ny))
     
            if graph[nx][ny] == 2:
                gram_distance = dist[x][y] + 1 + (n - 1 - nx) + (m - 1 - ny)

    return dist[n-1][m-1]

normal_path = bfs()
answer = min(normal_path if normal_path != -1 else float('inf'), gram_distance)

print(answer if answer <= t else 'Fail')