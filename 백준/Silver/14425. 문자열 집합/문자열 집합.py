N, M = map(int, input().split())
sentence = set()
cnt = 0 

for _ in range(N):
    s = input()
    sentence.add(s)

for _ in range(M):
    word = input()
    if word in sentence:
        cnt += 1 

print(cnt)