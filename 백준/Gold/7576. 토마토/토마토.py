from collections import deque
M, N = map(int, input().split())
tomato = [list(map(int, input().split())) for _ in range(N)]

dx = [0, 0, -1, 1]
dy = [-1, 1, 0, 0]

def bfs():
    queue = deque()

    for i in range(N):
        for j in range(M):
            if tomato[i][j] == 1:
                queue.append((i, j))

    while queue:
        x, y = queue.popleft()

        for d in range(4):
            nx = x + dx[d]
            ny = y + dy[d]

            if 0 <= nx < N and 0 <= ny < M:
                if tomato[nx][ny] == 0:
                    tomato[nx][ny] = tomato[x][y] + 1
                    queue.append((nx, ny))

    max_day = 1
    for i in range(N):
        for j in range(M):
            if tomato[i][j] == 0:
                return -1
            if tomato[i][j] > max_day:
                max_day = tomato[i][j]

    return max_day - 1

print(bfs())