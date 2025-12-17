n = int(input())
result = [list(map(int, input().split())) for _ in range(n)]

for nums in result:
    m = nums[0]          
    scores = nums[1:]    

    avg = sum(scores) / m

    count = 0
    for s in scores:
        if s > avg:
            count += 1

    ratio = count / m * 100
    print(f"{ratio:.3f}%")