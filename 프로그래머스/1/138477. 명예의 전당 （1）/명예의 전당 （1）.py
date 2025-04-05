def solution(k, score):
    answer = []
    answer_list = []
    
    for i, value in enumerate(score):
        answer_list.append(value)
        if len(answer_list) > k:
            answer_list.remove(min(answer_list))
        answer.append(min(answer_list))        
    return answer