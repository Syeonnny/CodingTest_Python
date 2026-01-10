S = input()

from collections import Counter
counts = Counter(S)

odd_chars = [ch for ch, v in counts.items() if v % 2 == 1]
if len(odd_chars) > 1:
    print("I'm Sorry Hansoo")
else: 
    mid = odd_chars[0] if odd_chars else ""
    words = []
    for ch in sorted(counts.keys()):
        words.append(ch * (counts[ch] // 2))
    words = ''.join(words)
    print(words + mid + words[::-1])