def solution(number, limit, power):
    division_sum = []
    for i in range(1, number+1):
        count = 0 
        for j in range(1, int(i**0.5)+1):
            if i%j==0:
                count += 1
                if j!=i//j:
                    count += 1
        division_sum.append(count)

    for i, idx in enumerate(division_sum):
        if idx > limit:
            division_sum[i] = power
    return sum(division_sum)