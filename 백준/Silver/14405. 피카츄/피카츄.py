words = input()
i = 0

while i < len(words):
    if words[i:i+2] == 'pi' or words[i:i+2] == 'ka':
        i += 2
    elif words[i:i+3] == 'chu':
        i += 3
    else:
        print('NO')
        break
else:
    print('YES')