def solution(arr1, arr2):
    answer = []
    for i in range(len(arr1)):
        new_row = []
        for j in range(len(arr1[0])):
            new_row.append(arr1[i][j]+arr2[i][j])
        answer.append(new_row)
    return answer