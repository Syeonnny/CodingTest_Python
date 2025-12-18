A, B, V = map(int, input().split())

if V <= A:
    print(1)
else:
    print((V - A + (A - B) - 1) // (A - B) + 1)