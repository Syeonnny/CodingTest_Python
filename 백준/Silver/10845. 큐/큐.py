from collections import deque

N = int(input())
queue = deque()
output = []

for words in range(N):
    words = input().split()

    if words[0] == 'push':
        queue.append(words[1])
    elif words[0] == 'pop':
        output.append(queue.popleft() if queue else -1)
    elif words[0] == 'size':
        output.append(len(queue))
    elif words[0] == 'empty':
        output.append(0 if queue else 1)
    elif words[0] == 'front':
        output.append(queue[0] if queue else -1)
    elif words[0] == 'back':
        output.append(queue[-1] if queue else -1)

print(*output)