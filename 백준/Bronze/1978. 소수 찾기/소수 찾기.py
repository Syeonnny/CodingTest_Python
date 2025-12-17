N = int(input())
nums = map(int, input().split())
count = 0

for n in nums:
    if n < 2:
        continue

    is_prime = True
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            is_prime = False
            break
    if is_prime:
        count += 1

print(count)