def solution(n, arr1, arr2):
    answer = []
    for a, b in zip(arr1, arr2):
        bina = format(a, f'0{n}b')
        binb = format(b, f'0{n}b')
        line = ''
        for x, y in zip(bina, binb):
            if x == '1' or y == '1':
                line += '#'
            else:
                line += ' '
        answer.append(line)
    return answer