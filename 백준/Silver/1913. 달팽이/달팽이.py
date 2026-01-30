N = int(input())
target = int(input())
graph = [[0]*N for i in range(N)]

num = N**2
x, y = 0, 0 

dx = [1, 0, -1, 0]
dy = [0, 1, 0, -1]
d = 0 

while num >= 1:
    graph[x][y] = num
    if num == target: 
        tx, ty = x, y

    num -= 1  

    nx = x + dx[d]
    ny = y + dy[d]

    if not (0 <= nx < N and 0 <= ny < N and graph[nx][ny] == 0):
        d = (d+1) %4
        nx = x + dx[d]
        ny = y + dy[d]

    x, y = nx, ny

for row in graph:
    print(*row)
print(tx+1, ty+1)