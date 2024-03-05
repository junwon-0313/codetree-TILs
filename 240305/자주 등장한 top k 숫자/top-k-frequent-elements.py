n,k = map(int,input().split())
d = dict()
lst = list(map(int,input().split()))
for num in lst:
    if num in d:
        d[num]+=1
    else:
        d[num]=1

top_k = sorted(list(d.items()), key=lambda x:(-x[1],-x[0]))
# print(top_k)
for idx in range(k):
    print(top_k[idx][0], end =' ')