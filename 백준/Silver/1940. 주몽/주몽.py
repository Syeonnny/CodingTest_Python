import sys 

N = int(sys.stdin.readline())
M = int(sys.stdin.readline())
cnt = 0 

nums = []
while len(nums) < N:
    nums.extend(map(int, sys.stdin.readline().split()))

nums = sorted(nums)

L = 0 
R = len(nums) - 1

while L < R:
    if nums[L] + nums[R] == M:
        cnt += 1 
        L += 1
        R -= 1
    elif nums[L] + nums[R] < M:
        L += 1
    elif nums[L] + nums[R] > M:
        R -= 1

print(cnt)