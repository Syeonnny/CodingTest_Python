import sys
input = sys.stdin.readline

n, m = map(int, input().split())

parent = list(range(n + 1))
rank = [0] * (n + 1)

def find(x):
    if parent[x] != x:
        parent[x] = find(parent[x]) 
    return parent[x]

def union(a, b):
    rootA = find(a)
    rootB = find(b)
    if rootA == rootB:
        return

    if rank[rootA] < rank[rootB]:
        parent[rootA] = rootB
    elif rank[rootA] > rank[rootB]:
        parent[rootB] = rootA
    else:
        parent[rootB] = rootA
        rank[rootA] += 1

ans = []
for _ in range(m):
    f, a, b = map(int, input().split())
    if f == 0:
        union(a, b)
    else:
        ans.append("YES" if find(a) == find(b) else "NO")

print("\n".join(ans))