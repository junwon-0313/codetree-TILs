from itertools import combinations
n, k = map(int,input().split())
lst = list(map(int,input().split()))
d = dict()
for num in lst:
    if num not in d:
        d[num]=1
    else:
        d[num]+=1

ans = 0
# 세 수가 모두 같을 때
if k%3==0 and d[k//3]>=3:
    ans += (d[k//3]*(d[k//3]-1)* (d[k//3]-2))//6
# 두 수가 같을 때
for num in list(d.keys()):
    if k-2*num ==num:
        continue
    if k-2*num in d:
        ans += (d[num]*(d[num]-1))//2 * d[k-2*num]
# 모두 다를 때
for tmp in list(combinations(list(d.keys()), 3)):
    if k == sum(tmp):
        t = 1
        for num in tmp:
            t*=d[num]
        ans +=t

print(ans)