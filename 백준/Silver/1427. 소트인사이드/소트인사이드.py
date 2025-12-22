N = input()

s = sorted(str(N), reverse=True)
for ch in s:
    print(ch, end='')