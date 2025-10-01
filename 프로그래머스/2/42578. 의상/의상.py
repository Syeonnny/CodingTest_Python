def solution(clothes):
    count = {}
    mul = 1 
    for name, kind in clothes:
        if kind not in count:
            count[kind]=0
        count[kind] += 1
    for value in count.values():
        mul *= (value+1)
    return mul-1