def solution(arr):
    stack = []
    for i in range(len(arr)):
        if not stack or arr[i] != stack[-1]:
            stack.append(arr[i])
    return stack