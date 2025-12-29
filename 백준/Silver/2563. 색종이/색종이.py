board = [[False]*100 for _ in range(100)]

N = int(input())
for _ in range(N):
    x, y = map(int, input().split())
    for i in range(x, x+10): 
        for j in range(y, y+10):
            board[i][j] = True
    
print(sum(sum(row) for row in board))