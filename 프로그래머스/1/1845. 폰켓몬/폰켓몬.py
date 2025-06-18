def solution(nums):
    numbers = list(set(nums))
    if len(numbers) == (len(nums)//2):
        return len(numbers)
    elif len(numbers) >= (len(nums)//2):
        return len(nums)/2
    else:
        return len(numbers)