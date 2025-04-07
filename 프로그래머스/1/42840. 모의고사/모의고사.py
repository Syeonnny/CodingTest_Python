def solution(answers):
    answer = []
    one = [1,2,3,4,5] 
    two = [2,1,2,3,2,4,2,5]
    three = [3,3,1,1,2,2,4,4,5,5] 
    one_count, two_count, three_count = 0, 0, 0 
    
    for i in range(len(answers)):
        if answers[i] == one[i%len(one)]:
            one_count += 1
        if answers[i] == two[i%len(two)]:
            two_count += 1
        if answers[i] == three[i%len(three)]:
            three_count += 1    
            
    max_count = max(one_count, two_count, three_count)
    if max_count == one_count:
        answer.append(1)
    if max_count == two_count:
        answer.append(2)
    if max_count == three_count:
        answer.append(3)
    
    return answer