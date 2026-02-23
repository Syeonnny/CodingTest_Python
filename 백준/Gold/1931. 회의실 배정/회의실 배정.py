N = int(input())
meeting = [tuple(map(int, input().split())) for _ in range(N)]
meeting = sorted(meeting, key=lambda x: (x[1], x[0]))
cnt = 1
last_end = meeting[0][1]

for i in range(1, len(meeting)):
    if meeting[i][0] >= last_end:
        last_end = meeting[i][1]
        cnt += 1
        
print(cnt)