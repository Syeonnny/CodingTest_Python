def solution(number, k):
    stack = []
    count = 0
    for char in number:
        while stack and char > stack[-1] and count < k:
            stack.pop()
            count += 1
        stack.append(char)
    if count < k:
            stack = stack[:-(k-count)]
    return ''.join(stack)