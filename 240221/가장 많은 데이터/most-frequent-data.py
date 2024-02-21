n = int(input())
d = dict()
for _ in range(n):
    s = input()
    if s not in d:
        d[s]=1
    else:
        d[s]+=1
print(max(list(d.values())))