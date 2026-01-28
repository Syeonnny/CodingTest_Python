N = int(input())
a = list(map(int, input().split()))

dp = [1] * (N)

for i in range(1, N):
    for j in range(i):
        if a[j] < a[i]:
            dp[i] = max(dp[i], dp[j] + 1)
    
print(max(dp))