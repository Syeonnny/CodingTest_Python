N = int(input())

words = sorted(set(input() for _ in range(N)), key=lambda x: (len(x), x))
for s in words:
    print(s)