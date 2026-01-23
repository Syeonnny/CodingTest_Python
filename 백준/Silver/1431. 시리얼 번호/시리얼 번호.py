N = int(input())
guitar = [input() for _ in range(N)]

def sum_of_digits(s):
    total = 0
    for c in s:
        if c.isdigit():
            total += int(c)
    return total

guitar = sorted(guitar, key=lambda x:(len(x), sum_of_digits(x), x))
print(*guitar, sep='\n')