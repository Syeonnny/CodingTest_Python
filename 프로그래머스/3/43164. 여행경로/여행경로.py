def solution(tickets):
    answer = []
    tickets.sort()
    visited = [False] * len(tickets)
    
    def dfs(current, used, route):
        nonlocal answer
        route.append(current)
        if used == len(tickets):
            answer = route.copy()
            return True
        for i, (start, end) in enumerate(tickets):
            if not visited[i] and start ==current:
                visited[i] = True
                if dfs(end, used+1, route):
                    return True
                visited[i]=False
        route.pop()
        return False
    
    dfs("ICN", 0, [])
    return answer