def solution(prices):
    answer = [0] * len(prices)
    stack = []
    
    for i in range(0, len(prices)-1):
        while stack and prices[i] < prices[stack[-1]]:
            prev = stack.pop()
            answer[prev] = i - prev
        stack.append(i)
    for index in stack:
        answer[index] = (len(prices)-1) - index
    return answer