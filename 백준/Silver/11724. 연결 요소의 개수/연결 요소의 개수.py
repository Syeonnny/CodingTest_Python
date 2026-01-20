import sys 
from collections import deque
sys.setrecursionlimit(10**7)

input = sys.stdin.readline
N, M = map(int, input().split())

graph = [[] for _ in range(N+1)]

for _ in range(M):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

visited = [False] * (N+1)

queue = deque()
def bfs(graph, v, visited):
    queue.append(v)
    visited[v] = True
    while queue:
        v = queue.popleft()
        for i in graph[v]:
            if not visited[i]:
                visited[i] = True
                queue.append(i)
cnt = 0 
for i in range(1, N+1):
    if not visited[i]:
        cnt += 1
        bfs(graph, i, visited)

print(cnt)