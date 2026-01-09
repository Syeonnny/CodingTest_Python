import math
N = int(input())
trees = [int(input()) for _ in range(N)]

prev = trees[0]
diff = []
for i in trees[1:]:
    diff.append(i-prev)
    prev = i

diff_set = set(diff)
g = math.gcd(*diff_set)

cnt = 0 
for d in diff:
    cnt += (d // g) - 1

print(cnt)