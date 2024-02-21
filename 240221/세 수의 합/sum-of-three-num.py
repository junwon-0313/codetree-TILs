n, k = map(int,input().split())
lst = list(map(int,input().split()))
count = dict()
for num in lst:
    if num not in count:
        count[num]=1
    else:
        count[num]+=1

ans = 0
for i in range(n):
    count[lst[i]]-=1

    for j in range(i):
        diff = k-lst[i] - lst[j]

        if diff in count:
            ans += count[diff]
print(ans)