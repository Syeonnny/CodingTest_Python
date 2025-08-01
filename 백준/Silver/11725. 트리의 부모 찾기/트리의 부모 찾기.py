import sys 
input = sys.stdin.readline
sys.setrecursionlimit(10**6)

n = int(input())
tree = [[] for _ in range(n+1)]

for _ in range(n-1):
    a, b = map(int, input().split())
    tree[a].append(b)
    tree[b].append(a)

parent = [0] * (n + 1)

def dfs(node, parent_node):
    parent[node] = parent_node
    for child in tree[node]:
        if child != parent_node:
            dfs(child, node)
dfs(1,0)

for i in range(2, n+1):
    print(parent[i])