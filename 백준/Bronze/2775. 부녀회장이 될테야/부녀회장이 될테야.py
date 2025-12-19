T = int(input())

for _ in range(T):
    a = int(input())
    b = int(input())

    dp = [i for i in range(b+1)]  

    for _ in range(a):
        for i in range(1, b+1):
            dp[i] += dp[i-1]

    print(dp[b])