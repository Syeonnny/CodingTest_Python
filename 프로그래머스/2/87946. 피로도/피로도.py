from itertools import permutations
def solution(k, dungeons):
    count_list = []
    for i in permutations(dungeons, len(dungeons)):
        current_k = k 
        count = 0
        for j in i:
            if current_k >= j[0]:
                current_k -= j[1]
                count += 1
        count_list.append(count)
    return max(count_list)
