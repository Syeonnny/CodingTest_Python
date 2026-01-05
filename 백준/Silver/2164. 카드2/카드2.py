from collections import deque

queue = deque(range(1, int(input())+1)) 

while len(queue) > 1:
    queue.popleft()
    move = queue.popleft()
    queue.append(move)
print(queue[0])