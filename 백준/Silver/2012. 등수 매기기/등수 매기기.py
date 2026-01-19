import sys
input = sys.stdin.readline

N = int(input())
rank = []
for _ in range(N):
    rank.append(int(input()))

rank.sort()
total = 0
for i, value in enumerate(rank):
    total += abs(((i+1)-value))

print(total)