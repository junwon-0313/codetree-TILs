n,k = map(int,input().split())
lst = list(map(int,input().split()))

total = 0
for a in range(n):
    a1 = lst[a]
    for a2 in lst[:a]+lst[a+1:]:
        if a1+a2==k:
            total+=1
print(total//2)