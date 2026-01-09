import sys
N, M = list(map(int, sys.stdin.readline().split()))

memo = {}

for _ in range(N):
    address, password = list(sys.stdin.readline().split())
    memo[address] = password

output = []
for _ in range(M):
    output.append(memo[sys.stdin.readline().strip()])
    
sys.stdout.write('\n'.join(output))