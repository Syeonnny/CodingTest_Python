N, M = list(map(int, input().split()))
floor = [input() for _ in range(N)]

i, j = 0, 0
cnt = 0

for i in range(N):
    for j in range(M):
        if floor[i][j] == '-':
            if j ==0 or floor[i][j-1] != '-':
                cnt += 1
        elif floor[i][j] == '|':
            if i == 0 or floor[i-1][j] != '|':
                cnt += 1
print(cnt)