n, s = map(int,input().split())
lst = list(map(int,input().split()))
ans = max(s,sum(lst)) # 최대값으로 설정, lst의 총합보다 항상 s가 큼
# 전체 합에서 두 수를 뺀다. 그 결과와 s의 차이가 최소가 되게 한다. 
total= sum(lst)
for x in range(n):
    for y in range(x+1, n):
        diff = abs(s - (total - lst[x]-lst[y]))
        if diff<ans:
            ans=diff
print(ans)