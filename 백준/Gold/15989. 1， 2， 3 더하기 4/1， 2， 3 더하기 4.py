T = int(input())
nums = [int(input()) for _ in range(T)]

dp = [0] * 10001
dp[0] = 1 

max_n = max(nums)

for num in [1, 2, 3]:
    for i in range(num, max_n + 1):
        dp[i] += dp[i - num]

for n in nums:
    print(dp[n])