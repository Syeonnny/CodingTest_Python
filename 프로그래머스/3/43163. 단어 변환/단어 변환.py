from collections import deque

def solution(begin, target, words):
    visited = [False] * len(words)
    
    def can_convert(words1, words2):
        diff = 0
        for i in range(len(words1)):
            if words1[i] != words2[i]:
                diff += 1 
        return diff
    
    def bfs(begin, count): 
        queue = deque([(begin, count)])
        while queue:
            current_word, count = queue.popleft()
            if current_word == target:
                return count
            else:
                for idx, char in enumerate(words):
                    if not visited[idx] and can_convert(current_word, char) == 1:
                        queue.append((char, count+1))
                        visited[idx] = True
        return 0
    return bfs(begin, 0)