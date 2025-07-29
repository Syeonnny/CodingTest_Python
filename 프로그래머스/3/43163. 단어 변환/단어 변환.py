from collections import deque 

def solution(begin, target, words):
    answer = 0
    visited = [False] *len(words)
    queue = deque()
    queue.append((begin,0))
    
    def check(word1, word2):
        diff = 0 
        for i in range(len(word1)):
            if word1[i] != word2[i]:
                diff += 1
        if diff == 1:
            return True 
        return False
    
    def bfs():
        while queue:
            current = queue.popleft()
            if current[0] == target:
                return current[1]
            for i in range(len(words)):
                if not visited[i] and check(current[0], words[i]):
                    queue.append((words[i], current[1]+1))
                    visited[i] = True
        return 0
    return bfs()