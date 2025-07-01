from collections import deque
def solution(n, edge):
    graph = [[] for _ in range(n+1)]
    for a, b in edge:
        graph[a].append(b)
        graph[b].append(a)
        
    visited = [False] * (n+1)
    distance = [0] * (n+1)
    
    def bfs():
        queue = deque([1])
        visited[1] = True
        distance[1] = 0
        
        while queue:
            node = queue.popleft()
            for neighbor in graph[node]:
                if not visited[neighbor]:
                    visited[neighbor] = True
                    distance[neighbor] = distance[node] + 1
                    queue.append(neighbor)
    bfs()
    max_dist = max(distance)
    return distance.count(max_dist)