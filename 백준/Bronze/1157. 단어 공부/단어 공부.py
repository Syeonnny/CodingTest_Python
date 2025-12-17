words = input().upper()
n = {}
for ch in words:
    n[ch] = n.get(ch,0) + 1
max_val = max(n.values())
max_key = [key for key, value in n.items() if value == max_val]

if len(max_key) > 1: 
    print("?")
else: 
    print(max_key[0])