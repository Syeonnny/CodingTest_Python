def solution(name, yearning, photo):
    answer = []
    score_dic = dict(zip(name, yearning))
    for i in photo:
        count = 0
        for names in i:
            if names in score_dic: 
                count += score_dic[names]
        answer.append(count)
    return answer