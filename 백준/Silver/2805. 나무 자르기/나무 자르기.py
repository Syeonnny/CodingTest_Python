N, M = map(int, input().split())
trees = list(map(int, input().split()))

left = 0
right = max(trees)
mid = (left + right) // 2 
answer = 0 

while left <= right:
    s = 0
    mid = (left + right) // 2 

    for i in trees:
        if i > mid:
            s += i - mid

            if s >= M:
                break

    if s >= M:
        answer = mid
        left = mid + 1
        
    else: 
        right = mid - 1

print(answer)