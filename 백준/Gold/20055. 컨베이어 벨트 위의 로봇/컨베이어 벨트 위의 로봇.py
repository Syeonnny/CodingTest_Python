from collections import deque
N, K = map(int, input().split())
durable = deque(map(int, input().split()))

robot = deque([False] * N)
zero_count = durable.count(0)
ans = 0 

while zero_count < K:
    durable.rotate(1)
    robot.rotate(1)
    robot[N-1] = False
    
    for i in range(N-2, -1, -1):
        if robot[i] and not robot[i+1] and durable[i+1] >= 1:
            robot[i] = False
            robot[i+1] = True
            durable[i+1] -= 1

            if durable[i+1] == 0:
                zero_count += 1
    
    robot[N-1] = False

    if not robot[0] and durable[0] >= 1:
        robot[0] = True
        durable[0] -= 1

        if durable[0] == 0:
            zero_count += 1
            
    ans += 1

print(ans)