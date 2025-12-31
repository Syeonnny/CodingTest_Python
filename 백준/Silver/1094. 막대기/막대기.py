X = int(input())
sticks = [64]

while sum(sticks) > X:
    mini = min(sticks)
    sticks.remove(mini)
    
    half = mini // 2 
    sticks.append(half)
    sticks.append(half)

    if sum(sticks)-half >= X:
        sticks.remove(half)
    if sum(sticks) == X:
        break
print(len(sticks))