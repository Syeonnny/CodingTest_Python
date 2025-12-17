a, b, c = [int(input()) for _ in range(3)]
num = str(a * b * c)
numslist = {}
for i in num:
    numslist[i] = numslist.get(i, 0) + 1
for i in range(10): 
    print(numslist.get(str(i), 0))