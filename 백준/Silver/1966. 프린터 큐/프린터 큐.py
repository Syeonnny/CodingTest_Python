from collections import deque 
T = int(input())
ans = []

for _ in range(T):
    N, M = map(int, input().split())
    queue = deque()
    cnt = 0

    prior = []
    while len(prior) < N:
        prior.extend(map(int, input().split()))

    for i, p in enumerate(prior):
        queue.append((p, i == M))

    while queue:
        p, is_target = queue.popleft()

        if queue and p < max(x[0] for x in queue):
            queue.append((p, is_target))
        else:
            cnt += 1 
            if is_target:
                ans.append(cnt)
                break

print(*ans, sep='\n')