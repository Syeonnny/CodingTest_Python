def solution(numbers):
    numbers = map(str, numbers)
    numbers = sorted(numbers, key = lambda x: x*4, reverse=True)
    answer = ''.join(numbers)
    if numbers[0] == '0':
        return '0'
    return answer