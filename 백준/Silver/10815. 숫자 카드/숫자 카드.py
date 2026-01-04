import sys 

N = int(input())
nums = set(map(int, sys.stdin.readline().split()))

M = int(input())
check = list(map(int, sys.stdin.readline().split()))

ans = []
for n in check:
    if n in nums:
        ans.append(1)
    else:
        ans.append(0)
print(*ans, end ='')