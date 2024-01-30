n = int(input())

lst = [i for i in range(1,10)]
idx = 8
for _ in range(n):
    for _ in range(n):        
        print(lst[idx],end='')
        idx = (idx-1)%9
    print()