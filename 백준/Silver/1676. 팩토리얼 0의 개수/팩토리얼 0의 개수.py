N = int(input())

cnt = 0
d = 5
while d <= N:
    cnt += N // d
    d *= 5

print(cnt)