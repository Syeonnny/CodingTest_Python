N = int(input())
words = [input() for _ in range(N)]

cnt = 0 
for ch in words:
    seen = []
    prev = ''
    for s in ch:
        if s != prev:
            if s not in seen:
                seen.append(s)
                prev = s    
            else: 
                break
    else: cnt += 1
print(cnt)