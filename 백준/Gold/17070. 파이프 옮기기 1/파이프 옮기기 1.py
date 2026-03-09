import sys
input = sys.stdin.readline

n = int(input())
graph = [list(map(int, input().split())) for _ in range(n)]
dp = [[[0] * 3 for _ in range(n)] for _ in range(n)]

dp[0][1][0] = 1

for r in range(n):
    for c in range(n):
        if graph[r][c] == 1:
            continue

        # 가로 상태 오른쪽, 대각선 가능
        if dp[r][c][0] > 0:
            if c + 1 < n and graph[r][c + 1] == 0:
                dp[r][c + 1][0] += dp[r][c][0]

            if (r + 1 < n and c + 1 < n and
                graph[r][c + 1] == 0 and
                graph[r + 1][c] == 0 and
                graph[r + 1][c + 1] == 0):
                dp[r + 1][c + 1][2] += dp[r][c][0]

        # 세로 상태 아래, 대각선 가능
        if dp[r][c][1] > 0:
            if r + 1 < n and graph[r + 1][c] == 0:
                dp[r + 1][c][1] += dp[r][c][1]

            if (r + 1 < n and c + 1 < n and
                graph[r][c + 1] == 0 and
                graph[r + 1][c] == 0 and
                graph[r + 1][c + 1] == 0):
                dp[r + 1][c + 1][2] += dp[r][c][1]

        # 대각선 상태 오른쪽, 아래, 대각선 가능
        if dp[r][c][2] > 0:
            if c + 1 < n and graph[r][c + 1] == 0:
                dp[r][c + 1][0] += dp[r][c][2]

            if r + 1 < n and graph[r + 1][c] == 0:
                dp[r + 1][c][1] += dp[r][c][2]

            if (r + 1 < n and c + 1 < n and
                graph[r][c + 1] == 0 and
                graph[r + 1][c] == 0 and
                graph[r + 1][c + 1] == 0):
                dp[r + 1][c + 1][2] += dp[r][c][2]

print(sum(dp[n - 1][n - 1]))