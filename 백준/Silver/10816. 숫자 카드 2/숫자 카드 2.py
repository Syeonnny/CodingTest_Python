import sys
N = int(sys.stdin.readline())

nums = []
while len(nums) < N:
    nums.extend(map(int, sys.stdin.readline().split()))

nums_dict = {}
for n in nums:
    nums_dict[n] = nums_dict.get(n, 0) + 1

M = int(sys.stdin.readline())
checks = []

while len(checks) < M:
    checks.extend(map(int, sys.stdin.readline().split()))

for m in checks:
    if m not in nums_dict:
        print(0, end=' ')
    else: 
        print(nums_dict[m], end=' ')