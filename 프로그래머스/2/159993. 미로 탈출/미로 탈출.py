from collections import deque
def solution(maps):
    answer = 0
    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]
    n = len(maps)
    m = len(maps[0])
    
    for i in range(len(maps)):
        for j in range(len(maps[0])):
            if maps[i][j] == 'S':
                sx, sy = i, j
                
    def bfs(sx, sy, target):
        visited = [[False] * len(maps[0]) for _ in range(len(maps))]
        queue = deque()
        queue.append((sx, sy, 0))
        visited[sx][sy]= True
    
        while queue:
            x, y, dist = queue.popleft()
            
            if maps[x][y] == target:
                return (x, y, dist) 
            
            for i in range(4):
                nx = x + dx[i]
                ny = y + dy[i]
                
                if 0 <= nx < n and 0 <= ny < m:
                    if not visited[nx][ny] and maps[nx][ny] != 'X':
                        visited[nx][ny] = True
                        queue.append((nx, ny, dist+1))
                        
        return (-1, -1, -1)
    
    for i in range(n):
        for j in range(m):
            if maps[i][j] == 'S':
                sx, sy = i, j
                
    lx, ly, dist1 = bfs(sx, sy, 'L')
    if dist1 == -1: 
        return -1 
    
    ex, ey, dist2 = bfs(lx, ly, 'E')
    if dist2 == -1: 
        return -1
            
    return dist1 + dist2