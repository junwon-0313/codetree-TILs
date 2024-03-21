n = int(input())
lst_a = list(map(int,input().split()))
m = int(input())
lst_b = list(map(int,input().split()))
d = dict()
for num in lst_a:
    if num not in d:
        d[num] =1

for num in lst_b:
    if num in d:
        print(1)
    else:
        print(0)