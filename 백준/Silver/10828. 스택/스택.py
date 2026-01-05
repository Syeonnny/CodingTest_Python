import sys
input = sys.stdin.readline

N = int(input())
stack = []
out = []

for _ in range(N):
    cmd = input().split()
    op = cmd[0]

    if op == 'push':
        stack.append(int(cmd[1]))
    elif op == 'pop':
        out.append(str(stack.pop()) if stack else '-1')
    elif op == 'size':
        out.append(str(len(stack)))
    elif op == 'empty':
        out.append('0' if stack else '1')
    else:  # top
        out.append(str(stack[-1]) if stack else '-1')

sys.stdout.write('\n'.join(out))