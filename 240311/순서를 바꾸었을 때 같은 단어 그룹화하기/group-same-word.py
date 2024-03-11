n = int(input())
d = dict()
for _ in range(n):
    lst = list(input())
    lst.sort()
    k = tuple(lst)
    if k not in d:
        d[k]=1
    else:
        d[k]+=1

val_lst = list(d.values())
val_lst.sort(reverse=True)
print(val_lst[0])