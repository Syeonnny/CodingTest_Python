def solution(array, commands):
    answer = []
    for l in commands:
        new_array = sorted(array[l[0]-1:l[1]])
        answer.append(new_array[l[2]-1])
    return answer