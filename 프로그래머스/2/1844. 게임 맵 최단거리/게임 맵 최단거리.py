from collections import deque
def solution(maps):
    visited = [[False] * len(maps[0]) for _ in range(len(maps))]
    n,m  = len(maps), len(maps[0])
    directions = [(-1,0), (1,0), (0,-1), (0,1)]
    
    def bfs():
        queue = deque([(0,0,1)])
        while queue:
            curr = queue.popleft()
            x, y, dist = curr
            if x == n-1 and y == m-1:
                return dist
            else:
                for dx, dy in directions:
                    nx = x + dx
                    ny = y + dy
                    if 0 <= nx < n and 0 <= ny < m:
                        if maps[nx][ny] == 1 and not visited[nx][ny]:
                            visited[nx][ny] = True
                            queue.append((nx, ny, dist+1))
        return -1
    return bfs()
