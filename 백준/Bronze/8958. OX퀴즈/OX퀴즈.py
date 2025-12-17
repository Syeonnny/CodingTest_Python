n = int(input())
result = [input() for i in range(n)]

for i in result:
    total = 0
    seq = 0
    for j in i: 
        if j == 'O':
            seq += 1
            total += seq 
        else: 
            seq = 0
    print(total)