S = input()

prev = S[0]
zero, one = 0, 0
if S[0] == '0':
    zero = 1
else: 
    one = 1 
for ch in S[1:]:
    
    if ch != prev:
        if ch == '0':
            zero += 1
        else:
            one += 1
    prev = ch

print(min(zero, one))