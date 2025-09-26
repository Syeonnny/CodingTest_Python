from collections import deque
def solution(maps):
    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]
    
    n = len(maps)
    m = len(maps[0])
    
    visited =[[False]*m for _ in range(n)]
    queue = deque([(0, 0, 1)])
    visited[0][0] = True
    
    while queue: 
        x, y, dist = queue.popleft()
        
        if x == n-1 and y ==m-1:
            return dist
        
        for i in range(4):
            nx, ny = x + dx[i], y + dy[i]
            if 0 <= nx < n and 0 <= ny < m:
                if not visited[nx][ny] and maps[nx][ny] == 1: 
                    visited[nx][ny] = True
                    queue.append((nx, ny, dist+1))
    return -1