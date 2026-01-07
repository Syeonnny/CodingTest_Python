N, K = map(int, input().split())
money = []
while len(money) < N:
    money.append(int(input()))

money = sorted(money, reverse=True)
cnt = 0  

for coin in money:
    cnt += K // coin
    K %= coin

print(cnt)