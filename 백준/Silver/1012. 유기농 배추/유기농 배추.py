import sys
sys.setrecursionlimit(10**7)

input = sys.stdin.readline
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def dfs(x, y):
    if x <= -1 or x >= M or y <= -1 or y >= N:
        return False
    if not graph[x][y] or visited[x][y]:
        return False 
    
    visited[x][y] = True

    for d in range(4):
        nx = x + dx[d]
        ny = y + dy[d]
        dfs(nx, ny)

T = int(input())

for _ in range(T):
    M, N, K = map(int,input().split())

    graph = [[0]*N for _ in range(M)]
    visited = [[False]*N for _ in range(M)]

    for _ in range(K):
        a, b = map(int, input().split())
        graph[a][b] = 1

    cnt = 0
    for i in range(M):
        for j in range(N):
            if graph[i][j] == 1 and not visited[i][j]:
                cnt += 1
                dfs(i, j)
    print(cnt)