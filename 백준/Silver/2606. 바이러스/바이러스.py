C = int(input())
connect = int(input())

graph = [[] for _ in range(C+1)]
for _ in range(connect):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

visited = [False] * (C+1)

def dfs(graph, v, visited):
    visited[v] = True
    for i in graph[v]:
        if not visited[i]:
            dfs(graph, i, visited)

dfs(graph, 1, visited)
print(visited.count(True)-1)