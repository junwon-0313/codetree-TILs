# 최소 T번 이상 H 높이로 나오게끔 한다. 
n, h, t = map(int,input().split())
field = list(map(int,input().split()))

cost = []
for i in range(n):
    if field[i]==h:
        cost.append(0)
    else:
        cost.append(abs(field[i]-h))
min_cost = 200*100
for i in range(n-t+1):
    tmp_cost = 0
    for j in range(i,i+t):
        tmp_cost+=cost[j]
    if tmp_cost<min_cost:
        min_cost=tmp_cost
print(min_cost)