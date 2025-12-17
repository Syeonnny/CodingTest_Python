from collections import Counter

words = input().upper()
cnt = Counter(words)

max_char, max_val = cnt.most_common(1)[0]

if list(cnt.values()).count(max_val) > 1:
    print("?")
else:
    print(max_char)