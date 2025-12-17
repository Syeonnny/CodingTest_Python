words = input()
i = 0
cnt = 0
while i < len(words):
    if words[i:i+3] == 'dz=':
        i += 3
    elif words[i:i+2] in ['c=', 'c-', 'd-', 'lj', 'nj', 's=', 'z=']:
        i += 2
    else:
        i += 1
    cnt += 1 
print(cnt)