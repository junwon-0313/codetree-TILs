# 3개의 자리로 그룹을 나눈다.
# 자리수로 구별

n,m = map(int, input().split())
groupA =[]
groupB =[]
for _ in range(n):
    groupA.append(input())

for _ in range(n):
    groupB.append(input())
# 50*50*50*500
ans =0
for i in range(m):
    for j in range(i+1,m):
        for k in range(j+1,m):
            sa = set()
            sb = set()
            for s in range(n):
                a = groupA[s][i]+groupA[s][j]+groupA[s][k]
                b = groupB[s][i]+groupB[s][j]+groupB[s][k]
                sa.add(a)
                sb.add(b)
            if not sa.intersection(sb):
                ans+=1

print(ans)