def solution(answers):
    answer = []
    length = len(answers)
    one = [1,2,3,4,5]*length
    two = [2,1,2,3,2,4,2,5]*length
    three = [3,3,1,1,2,2,4,4,5,5]*length
    
    one_counts, two_counts, three_counts = 0,0,0
    for i in range(length):
        if one[i] == answers[i]:
            one_counts += 1
    for i in range(length):
        if two[i] == answers[i]:
            two_counts += 1
    for i in range(length):
        if three[i] == answers[i]:
            three_counts += 1
    
    max_num = max(one_counts, two_counts, three_counts)
    if max_num == one_counts:
        answer.append(1)
    if max_num == two_counts:
        answer.append(2)
    if max_num == three_counts:
        answer.append(3)
    return answer