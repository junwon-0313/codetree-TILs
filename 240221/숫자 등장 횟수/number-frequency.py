n, m = map(int, input().split())

num_lst = list(map(int, input().split()))
cnt_lst = list(map(int, input().split()))

d = dict()
for num in num_lst:
    if num not in d:
        d[num]=1
    else:
        d[num]+=1

for num in cnt_lst:
    if num not in d:
        print(0, end = '')
    else:
        print(d[num], end = ' ')