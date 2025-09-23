def solution(s):
    s = s.lower()
    p_num, y_num = 0, 0
    for i in s:
        if i=='p':
            p_num += 1 
        elif i=='y':
            y_num += 1
    return p_num == y_num