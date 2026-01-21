import sys
input = sys.stdin.readline

N, M = map(int, input().strip().split())
trees = list(map(int, input().strip().split()))

low = 0
high = max(trees)
candidate = 0 

while low <= high:
    H = (low + high) // 2 
    d = 0 
    for i in trees:
        if i > H:
            d += (i-H)
            if d >= M:
                break 
    
    if d >= M:
        candidate = H
        low = H + 1
    else:
        high = H - 1
    
print(candidate)