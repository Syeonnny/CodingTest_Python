from collections import deque

dx = [-1, -1, -1,  0, 0,  1, 1, 1]
dy = [-1,  0,  1, -1, 1, -1, 0, 1]

def bfs(x, y):
    queue = deque()
    queue.append((x, y))
    visited[x][y] = True

    while queue: 
        x, y = queue.popleft()
        for d in range(8):
            nx = x + dx[d]
            ny = y + dy[d]

            if nx < 0 or ny < 0 or nx >= h or ny >= w:
                continue

            if graph[nx][ny] == 1 and not visited[nx][ny]:
                visited[nx][ny] = True
                queue.append((nx,ny))
                

while True:
    w, h = map(int, input().split())
    if w == 0 and h == 0:
        break
    graph = [list(map(int, input().split())) for _ in range(h)]
    visited = [[False]*w for _ in range(h)]
    cnt = 0

    for x in range(h):
        for y in range(w):
            if graph[x][y] == 1 and not visited[x][y]:
                cnt += 1
                bfs(x, y)
    print(cnt)