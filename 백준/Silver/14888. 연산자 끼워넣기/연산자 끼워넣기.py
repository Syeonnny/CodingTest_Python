N = int(input())
nums = list(map(int, input().split()))
plus, minus, mul, div = map(int, input().split())

max_value = -int(1e9)
min_value = int(1e9)

def dfs(idx, cur, plus, minus, mul, div):
    global max_value, min_value

    if idx == N:
        max_value = max(max_value, cur)
        min_value = min(min_value, cur)
        return 
    
    if plus > 0:
        dfs(idx+1, cur + nums[idx], plus-1, minus, mul, div)

    if minus > 0:
        dfs(idx+1, cur - nums[idx], plus, minus-1, mul, div)

    if mul > 0:
        dfs(idx+1, cur * nums[idx], plus, minus, mul-1, div)

    if div > 0:
        dfs(idx+1, int(cur / nums[idx]), plus, minus, mul, div-1)

dfs(1, nums[0], plus, minus, mul, div)
print(max_value)
print(min_value)