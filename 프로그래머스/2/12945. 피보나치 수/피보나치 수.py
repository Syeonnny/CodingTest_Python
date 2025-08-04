def solution(n):
    fibo = [0, 1]
    i = 2
    while i<=n:
        fibo.append(fibo[-1]+fibo[-2])
        i += 1
    return fibo[-1] % 1234567