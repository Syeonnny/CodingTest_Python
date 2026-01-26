import sys 
input = sys.stdin.readline

N = int(input())
nums = list(map(int, input().split()))
nums_set = sorted(set(nums))
nums_dict = {}

for i, val in enumerate(nums_set):
    nums_dict[val] = i

ans = []
for n in nums:
    ans.append(nums_dict[n])

print(*ans)