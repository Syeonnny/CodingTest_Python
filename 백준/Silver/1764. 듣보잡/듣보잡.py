N, M = map(int, input().split())

listen = set()
see = set()

for i in range(N+M):
    names = input()
    if i <= N-1:
        listen.add(names)
    else:
        see.add(names)

output = sorted(listen & see)
print(len(output))
print(*output,sep='\n')