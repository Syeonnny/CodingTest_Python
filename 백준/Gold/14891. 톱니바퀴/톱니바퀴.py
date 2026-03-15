from collections import deque
import sys

input = sys.stdin.readline

gears = [deque(input().strip()) for _ in range(4)]

k = int(input())

for _ in range(k):
    num, direction = map(int, input().split())
    num -= 1  

    rotate_dir = [0] * 4
    rotate_dir[num] = direction

    for i in range(num, 0, -1):
        if gears[i][6] != gears[i - 1][2]:
            rotate_dir[i - 1] = -rotate_dir[i]
        else:
            break

    for i in range(num, 3):
        if gears[i][2] != gears[i + 1][6]:
            rotate_dir[i + 1] = -rotate_dir[i]
        else:
            break

    for i in range(4):
        if rotate_dir[i] != 0:
            gears[i].rotate(rotate_dir[i])

score = 0
for i in range(4):
    if gears[i][0] == '1':
        score += (1 << i)

print(score)