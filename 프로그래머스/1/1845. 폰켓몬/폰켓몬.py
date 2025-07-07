def solution(nums):
    num = len(nums)//2
    set_nums = set(nums)
    return min(num, len(set_nums))