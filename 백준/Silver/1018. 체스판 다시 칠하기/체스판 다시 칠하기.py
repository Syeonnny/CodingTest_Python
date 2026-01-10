N, M = map(int, input().split())
board = [input() for _ in range(N)]
cnt = []
for a in range(N-7):
    for b in range(M-7):
        paint1 = 0
        paint2 = 0
        for i in range(a, a+8):
            for j in range(b, b+8):
                if (i+j) % 2 == 0:
                    if board[i][j] != 'W':
                        paint1 += 1
                    if board[i][j] != 'B':
                        paint2 += 1
                else:
                    if board[i][j] != 'B':
                        paint1 += 1
                    if board[i][j] != 'W':
                        paint2 += 1
        cnt.append(min(paint1, paint2))

print(min(cnt))