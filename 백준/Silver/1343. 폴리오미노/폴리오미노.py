s = input()

valid = True
i = 0
output = [None] * len(s)

while i < len(s):
    if s[i] == '.':
        output[i] = '.'
        i += 1
    else:
        if s[i:i+4] == 'XXXX':
            output[i:i+4] = 'AAAA'
            i += 4
        elif s[i:i+2] == 'XX':
            output[i:i+2] = 'BB'
            i += 2
        else:
            valid = False
            break

print("".join(output) if valid else -1)