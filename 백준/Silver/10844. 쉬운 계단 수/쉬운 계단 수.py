N = int(input())
dp = [0] * 10

for i in range(1, 10):
    dp[i] = 1

for _ in range(2, N + 1):
    nxt = [0] * 10
    for d in range(10):
        if d - 1 >= 0:
            nxt[d] += dp[d - 1]
        if d + 1 <= 9:
            nxt[d] += dp[d + 1]
        nxt[d] %= 1000000000
    dp = nxt

print(sum(dp) % 1000000000)