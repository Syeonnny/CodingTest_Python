from itertools import combinations

N, M = map(int, input().split())
cities = [list(map(int, input().split())) for _ in range(N)]

homes = []
chicken = []

for i in range(N):
    for j in range(N):
        if cities[i][j] == 1:
            homes.append((i,j))
        elif cities[i][j] == 2:
            chicken.append((i,j))


ans = []
dist = [[0] * len(chicken) for _ in range(len(homes))]

for hi, (r1, c1) in enumerate(homes):
    for ci, (r2, c2) in enumerate(chicken):
        dist[hi][ci] = abs(r1-r2) + abs(c1-c2)

best = float('inf')

for comb in combinations(range(len(chicken)), M):
    total = 0
    for hi in range(len(homes)):
        total += min(dist[hi][ci] for ci in comb)
        if total >= best: 
            break
    best = min(best, total)

print(best)