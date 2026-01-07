import sys 

N, M = map(int, sys.stdin.readline().split())

nums = []
while len(nums) < N:
    nums.extend(map(int, sys.stdin.readline().split()))

cnt, total = 0, 0 
L, R = 0, 0

while True:
    if total >= M:
        if total == M:
            cnt += 1
        total -= nums[L]
        L += 1
    else:
        if R == N:
            break
        total += nums[R]
        R += 1

print(cnt)