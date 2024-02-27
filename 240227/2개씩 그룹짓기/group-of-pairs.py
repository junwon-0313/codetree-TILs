# 정렬 후, 앞에서 뒤랑 매칭해서 더해서 최댓값
n = int(input())
lst = list(map(int, input().split()))
lst.sort()
ans = 0
for idx in range(n):
    tmp = lst[idx]+lst[-1-idx]
    if ans<tmp:
        ans=tmp
print(ans)