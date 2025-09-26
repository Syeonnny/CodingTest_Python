def solution(n):
    answer = 0
    for x in range(2, n+1):
        prime = True
        for i in range(2, int(x**0.5)+1):
            if x % i ==0:
                prime = False
                break
        if prime:
            answer += 1 
    return answer