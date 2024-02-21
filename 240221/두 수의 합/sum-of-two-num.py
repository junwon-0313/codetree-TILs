n, k = map(int, input().split())
lst = list(map(int, input().split()))
d = dict()
for num in lst:
    if num not in d:
        d[num]=1
    else:
        d[num]+=1

ans =0
for num in list(d.keys()):
    if k-num in d:
        ans += d[num]*d[k-num]
print(ans//2)