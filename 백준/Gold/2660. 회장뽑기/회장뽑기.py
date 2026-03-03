import sys
input = sys.stdin.readline

INF = int(1e9)
n = int(input())
dist = [[INF] * (n+1) for _ in range(n+1)]

for i in range(1, n+1):
    dist[i][i] = 0

while True:
    a, b = map(int, input().split())
    if a == -1 and b == -1:
        break
    dist[a][b] = 1
    dist[b][a] = 1

for k in range(1, n+1):
    for i in range(1, n+1):
        for j in range(1, n+1):
            if dist[i][j] > dist[i][k] + dist[k][j]:
                dist[i][j] = dist[i][k] + dist[k][j]

scores = []
for i in range(1, n+1):
    score = max(dist[i][1:])   
    scores.append(score)

min_sc = min(scores)

cand = []
for i in range(n):
    if scores[i] == min_sc:
        cand.append(i+1)

print(min_sc, len(cand))
print(*cand)