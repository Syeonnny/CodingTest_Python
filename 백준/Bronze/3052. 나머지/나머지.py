n = [int(input()) for _ in range(10)]
nums = []
for i in n:
    nums.append(i % 42)
nums = set(nums)
print(len(nums))