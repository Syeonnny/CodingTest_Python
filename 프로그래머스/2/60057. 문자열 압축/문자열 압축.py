def solution(s):
    answer_list = []
    if s == "": 
        return 0
    if len(s) == 1:
        return 1
    
    for k in range(1, len(s)//2+1):
        answer = ''
        count = 1
        prev = s[0:k]
        
        for i in range(k, len(s), k):
            cur = s[i:i+k]
            if cur == prev:
                count += 1
            else: 
                if count > 1:
                    answer += str(count)+prev
                else:
                    answer += prev
                prev=cur
                count = 1 
                
        if count > 1:
            answer += str(count)+prev
        elif count == 1:
            answer += prev
        answer_list.append(len(answer)) 
    return min(answer_list)