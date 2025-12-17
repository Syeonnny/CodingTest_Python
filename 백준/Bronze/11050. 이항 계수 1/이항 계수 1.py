n, r = map(int, input().split())
r = min(r, n - r)

ans = 1
for i in range(1, r + 1):
    ans = ans * (n - r + i) // i

print(ans)