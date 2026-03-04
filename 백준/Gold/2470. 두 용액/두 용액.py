N = int(input())
sol = sorted(map(int, input().split()))

left = 0
right = N-1
candidate = abs(sol[left] + sol[right])
a, b = sol[left], sol[right]

while left < right:
    total = sol[left] + sol[right]

    if abs(total) < candidate:
        candidate = abs(total)
        a, b = sol[left], sol[right]

    if total < 0:
        left += 1
    else:
        right -= 1

print(a, b)