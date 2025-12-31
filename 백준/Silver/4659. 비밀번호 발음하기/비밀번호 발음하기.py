while True:
    pw = input()

    if pw == 'end':
        break
    accept = True
    
    v = ['a', 'e', 'i', 'o', 'u']

    n = 0 
    for s in pw:
        if s in v:
            n += 1
    if n == 0:
        accept = False

    prev_type = 'V' if pw[0] in v else 'C'
    cnt = 1

    if accept: 
        for c in pw[1:]:
            cur_type = 'V' if c in v else 'C'
            if cur_type == prev_type:
                cnt += 1
            else:
                cnt = 1
                prev_type = cur_type

            if cnt == 3:
                accept = False
                break
    if accept:
        for i in range(len(pw)-1):
            prev = pw[i]
            seq = pw[i+1]
            if prev == seq and prev not in ['e', 'o']:
                accept = False
                break
            
    if accept == True:
        print(f'<{pw}> is acceptable.')
    else: 
        print(f'<{pw}> is not acceptable.')     