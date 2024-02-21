n, m = map(int,input().split())
d = dict()
for idx in range(1,n+1):
    s = input()
    d[str(idx)] = s
    d[s] = idx

for _ in range(m):
    s = input()
    print(d[s])