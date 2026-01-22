import sys
input = sys.stdin.readline

n = int(input())
stack = []
ans = []

seq = [int(input().strip()) for _ in range(n)]
    
w = 1
for target in seq:
    while w <= target:
        stack.append(w)
        ans.append('+')
        w += 1
    if stack and stack[-1] == target:
        stack.pop()
        ans.append('-')
    elif stack[-1] != target:
        print("NO")
        sys.exit()
print(*ans, sep='\n')