N, M = map(int, input().split())
r, c, d = map(int, input().split())

rooms = [list(map(int, input().split())) for _ in range(N)]

dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

cnt = 0 

while True: 
    if rooms[r][c] == 0:
        rooms[r][c] = 2
        cnt += 1

    moved = False
    for _ in range(4):
        d = (d+3) % 4
        nr = r + dx[d]
        nc = c + dy[d]

        if 0 <= nr < N and 0 <= nc < M and rooms[nr][nc] == 0: 
            r, c = nr, nc
            moved = True
            break

    if not moved:
        back = (d+2)%4
        br = r + dx[back]
        bc = c + dy[back]

        if rooms[br][bc] == 1:
            break
        
        r,c = br, bc 

print(cnt)