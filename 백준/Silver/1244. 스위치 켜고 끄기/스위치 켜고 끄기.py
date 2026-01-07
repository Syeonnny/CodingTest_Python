import sys 

switch_num = int(sys.stdin.readline().strip())
switch = []

while len(switch) < switch_num:
    switch.extend(map(int, sys.stdin.readline().split()))

student_num = int(sys.stdin.readline().strip())

for _ in range(student_num):
    gen_num = list(map(int, sys.stdin.readline().split()))
    if gen_num[0] == 1:
        idx = gen_num[1]
        for m in range(idx-1, switch_num, idx): 
            switch[m] = 1 - switch[m]

    else:
        idx = gen_num[1] - 1
        L = R = idx
        while L-1 >= 0 and R+1 < switch_num and switch[L-1] == switch[R+1]: 
            L -= 1
            R += 1
            
        for i in range(L, R+1):
            switch[i] = 1 - switch[i]

for i in range(0, switch_num, 20):
        print(*switch[i:i+20])