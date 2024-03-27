n = int(input())
lst = list(map(int,input().split()))

d = dict()
for idx, num in enumerate(sorted(lst)):
    if num not in d:
        d[num]=[idx+1]
    else:
        d[num].append(idx+1)

for num in lst:
    print(d[num][0], end=' ')
    d[num].pop(0)