N = int(input())
num = int(input())

boards = [[0]*N for _ in range(N)]

dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

x = N//2
y = N//2
d = 0 

idx = 1 
boards[x][y] = idx

if idx == num:
    num_ans = [x+1, y+1]

step = 1
while idx < N**2:
    for _ in range(2):
        for _ in range(step):
            if idx == N**2:
                break
            x += dx[d]
            y += dy[d]
            idx += 1
            boards[x][y] = idx
            if idx == num:
                num_ans = [x+1, y+1]
        d = (d+1) % 4
    step += 1

for row in boards:
    print(*row)
print(*num_ans)