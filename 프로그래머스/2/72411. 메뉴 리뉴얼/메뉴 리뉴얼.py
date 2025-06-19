from collections import Counter
from itertools import combinations

def solution(orders, course):
    answer = []
    for i in course:
        comb_list = Counter()
        for j in range(len(orders)):
            comb_list += Counter(combinations(sorted(orders[j]), i))
        if comb_list:
            max_count = comb_list.most_common(1)[0][1]
            if max_count >= 2:
                for comb, cnt in comb_list.items():
                    if cnt == max_count:
                        answer.append(''.join(comb))
    answer.sort()
    return answer
