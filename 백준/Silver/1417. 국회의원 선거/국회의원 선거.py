N = int(input())
score = []
for i in range(N):
    score.append(int(input()))

win = score.pop(0)
cnt = 0

if not score:
    print(cnt)
else: 
    while win <= max(score):
        max_score = score.index(max(score))
        score[max_score] -= 1
        win += 1
        cnt += 1 
    print(cnt)