N = int(input())
guitar = [input() for _ in range(N)]
number = [str(i) for i in range(1,10)]

def sum_of_digits(s):
    total = 0
    for i in s:
        if i in number:
            total += int(i)
    return total
    
guitar = sorted(guitar, key=lambda x:(len(x), sum_of_digits(x), x))
print(*guitar, sep='\n')