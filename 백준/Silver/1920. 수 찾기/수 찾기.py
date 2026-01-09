import sys
N = int(sys.stdin.readline())
n_nums = set(map(int, sys.stdin.readline().split()))

M = int(sys.stdin.readline())
m_nums = list(map(int, sys.stdin.readline().split()))

output = []
for n in m_nums: 
    if n in n_nums:
        output.append('1') 
    else:
        output.append('0')

sys.stdout.write('\n'.join(output))