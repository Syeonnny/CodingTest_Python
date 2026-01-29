N, K = map(int, input().split())
nums = [int(input()) for _ in range(N)]
nums.sort() 

low = 1
high = max(nums)
ans = 0

while low <= high:
    mid = (low + high) // 2
    cnt = 0 

    for i in nums: 
        cnt += i // mid 

    if cnt >= K:
        ans = mid
        low = mid + 1
    else:
        high = mid -1
print(ans)