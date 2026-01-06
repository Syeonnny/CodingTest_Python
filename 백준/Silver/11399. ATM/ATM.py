import sys 
N = int(sys.stdin.readline())
nums = []
while len(nums) < N:
    nums.extend(map(int, sys.stdin.readline().split()))

nums = sorted(nums)
total = 0
answer = 0 
for i in nums:
    total += i
    answer += total
print(answer)