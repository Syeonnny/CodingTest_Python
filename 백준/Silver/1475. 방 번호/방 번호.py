import sys

N = sys.stdin.readline().strip()

others = {}
six_nine = 0

for ch in N:
    if ch == '6' or ch == '9':
        six_nine += 1
    else:
        others[ch] = others.get(ch, 0) + 1

six_nine = (six_nine + 1) // 2
others_max = max(others.values(), default=0)

print(max(others_max, six_nine))