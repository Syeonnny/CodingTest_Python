N, M = map(int, input().split())
key_name = {}
key_num = {}

for i in range(1, N+1):
    name = input()
    key_num[i] = name
    key_name[name] = i

for _ in range(M):
    form = input()
    if form.isdigit():
        print(key_num[int(form)])
    else:
        print(key_name[form])