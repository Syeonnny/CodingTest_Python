N, L = map(int, input().split())
location = sorted(list(map(int, input().split())))

end_L = location[0] + L - 1 
cnt = 1 

for i in range(1, len(location)):
    if location[i] > end_L:
        cnt += 1
        end_L = location[i] + L -1

print(cnt)