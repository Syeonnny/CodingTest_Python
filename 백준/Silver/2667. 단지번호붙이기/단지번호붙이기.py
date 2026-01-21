import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**7)

N = int(input())

graph = [list(map(int, input().strip())) for _ in range(N)]
visited = [[0]*N for _ in range(N)]

homes = []
homes_num = 0 

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def dfs(x, y):
    cnt = 1
    if x >= N or y >= N or x < 0 or y < 0:
        return 0
    
    if visited[x][y] or not graph[x][y]: 
        return 0
    
    visited[x][y] = True

    for d in range(4):
        nx = x + dx[d]
        ny = y + dy[d]
        cnt += dfs(nx, ny) 

    return cnt


for x in range(N):
    for y in range(N):
        if not visited[x][y] and graph[x][y] == 1:
            homes_num += 1
            homes.append(dfs(x, y))

print(homes_num)
homes.sort()
print(*homes, sep='\n')