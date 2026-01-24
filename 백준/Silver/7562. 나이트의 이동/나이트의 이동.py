from collections import deque

dx = [-2, -1, 1, 2, 2, 1, -1, -2]
dy = [1, 2, 2, 1, -1, -2, -2, -1]

def bfs(x, y):
    # dist = [[0] * I for _ in range(I)]
    queue = deque([(x,y)])

    while queue:
        x, y = queue.popleft()
        if x == wx and y == wy:
            return graph[wx][wy]
        
        for d in range(8):
            nx = x + dx[d]
            ny = y + dy[d]

            if nx < 0 or ny < 0 or nx >= I or ny >= I:
                continue
            if graph[nx][ny] == 0:
                graph[nx][ny] = graph[x][y] + 1
                queue.append((nx,ny))

T = int(input())
for _ in range(T):
    I = int(input())
    graph = [[0] * I for _ in range(I)]
    x, y = map(int, input().split())
    wx, wy = map(int, input().split()) 

    print(bfs(x, y))