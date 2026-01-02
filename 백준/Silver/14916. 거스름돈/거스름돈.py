n = int(input())

coin = n // 5  

while coin >= 0:
    rest = n - 5 * coin  
    if rest % 2 == 0:
        coin += rest // 2
        print(coin)
        break
    coin -= 1
else:
    print(-1)