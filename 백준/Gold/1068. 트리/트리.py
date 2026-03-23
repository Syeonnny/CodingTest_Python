import sys
input = sys.stdin.readline

N = int(input())
parents = list(map(int, input().split()))
remove = int(input())

tree = [[] for _ in range(N)]
root = 0

for i in range(N):
    if parents[i] == -1:
        root = i
    else:
        tree[parents[i]].append(i)

if remove == root:
    print(0)
    exit()

leaf_count = 0

def dfs(x):
    global leaf_count
    child_count = 0

    for nx in tree[x]:
        if nx == remove:
            continue
        child_count += 1
        dfs(nx)

    if child_count == 0:
        leaf_count += 1

dfs(root)

print(leaf_count)