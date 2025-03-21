def solution(brown, yellow):
    num = brown+yellow
    nums_list = []
    for i in range(1,num):
        if num%i == 0:
            w = num//i
            h = i
            nums_list.append([w,h])
            if (w-2) * (h-2) == yellow:
                return [w,h]
