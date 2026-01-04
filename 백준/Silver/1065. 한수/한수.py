N = int(input())
cnt = 0

for i in range(1, N+1):    
    s = str(i)

    if len(s) <= 2:
        cnt += 1

    else: 
        complete = True
        d = int(s[1]) - int(s[0])

        for k in range(2, len(s)):
            if int(s[k]) - int(s[k - 1]) != d:
                complete = False
                break

        if complete:
            cnt += 1

print(cnt)