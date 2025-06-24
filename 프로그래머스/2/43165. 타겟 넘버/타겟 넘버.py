def solution(numbers, target):
    count = 0
    def dfs(index, total):
        nonlocal count
        if index == len(numbers):
            if total == target:
                count += 1
            return
        dfs(index+1, total - numbers[index])
        dfs(index+1, total + numbers[index])
    dfs(0,0)
    return count