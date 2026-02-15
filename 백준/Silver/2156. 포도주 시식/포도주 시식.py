n = int(input())
q = [int(input()) for _ in range(n)]
if n == 1:
    print(q[0])
elif n == 2:
    print(q[0]+q[1])
else: 
    dp = [0] * n 
    dp[0] = q[0]
    dp[1] = q[0] + q[1]
    dp[2] = max(q[0] + q[1], 
                q[1] + q[2],
                q[0] + q[2])

    for i in range(3, n):
        dp[i] = max(dp[i-1], 
                    dp[i-2] + q[i], 
                    dp[i-3] + q[i-1] + q[i]) 
    
    print(dp[n-1])