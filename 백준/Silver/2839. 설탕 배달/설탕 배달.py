N = int(input())
cnt = 0
complete = False 
five = N // 5
while five >= 0:
    rem = N - 5 * five
    if rem == 0:
        cnt += five
        complete = True
        break
    elif rem % 3 == 0:
        cnt += five
        cnt += rem // 3
        complete = True
        break
    else:
        five -= 1
print(cnt if complete else -1)