import sys
input = sys.stdin.readline

n = int(input())
ans = [int(input()) for _ in range(n)] 

st = []
cur = 1
ops = []

for target in ans:
    while cur <= target:
        st.append(cur)
        cur += 1
        ops.append('+')

    if st and st[-1] == target:
        st.pop()
        ops.append('-')
    else:
        print("NO")
        sys.exit(0)

print("\n".join(ops))