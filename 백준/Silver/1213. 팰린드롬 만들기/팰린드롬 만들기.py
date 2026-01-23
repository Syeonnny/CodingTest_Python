s = input()
s_dict = {}
for ch in s:
    s_dict[ch] = s_dict.get(ch, 0) + 1

odd_cnt = 0
mid = ''

for v in s_dict.values():
    if v % 2 == 1:
        odd_cnt += 1

if odd_cnt > 1:
    print("I'm Sorry Hansoo")

else: 
    left = []
    mid = ''

    for ch in sorted(s_dict.keys()):
        repeat = s_dict[ch] // 2
        left.append(ch * repeat)

        if s_dict[ch] % 2 == 1:
            mid = ch

    ans = "".join(left) + mid + "".join(left[::-1])
    print(ans)