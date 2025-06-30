def solution(n, computers):
    visited = [False] * n
    count = 0
    def dfs(node):
        for i in range(n):
            if computers[node][i] == 1 and not visited[i]:
                visited[i] = True
                dfs(i)
    for i in range(n):
        if not visited[i]:
            dfs(i)
            count += 1
    return count