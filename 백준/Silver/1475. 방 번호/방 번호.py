N = input()
cnt = 0

others = {}

for i in N:
    if int(i) not in [6, 9]:
        others[i] = others.get(i, 0) + 1

six_nine = (int(N.count('6') + N.count('9')) + 1) // 2

others_max = max(others.values(), default = 0)
cnt = max(others_max, six_nine)   
print(cnt)