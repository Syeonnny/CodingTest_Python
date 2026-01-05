T = int(input())
for s in range(T):
    s = input()
    stack = []
    complete = True
    for ch in s:
        if ch=='(':
            stack.append(ch)
        elif stack and ch == ')':
            stack.pop()
        else:    
            complete = False
            break
    if stack:
        complete = False
    print('YES' if complete else 'NO')