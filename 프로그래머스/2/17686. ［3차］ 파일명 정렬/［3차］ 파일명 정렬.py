def solution(files):
    answer = []
    for idx, name in enumerate(files):
        i, n = 0, len(name)
        
        while i < n and not name[i].isdigit():
            i += 1 
        head = name[:i].lower()
        
        j, cnt = i, 0 
        
        while j < n and name[j].isdigit() and cnt < 5:
            j += 1
            cnt += 1
        num = int(name[i:j])

        answer.append((head, num, idx, name))
        
    answer.sort(key = lambda x:(x[0], x[1], x[2]))
    return [t[3] for t in answer]