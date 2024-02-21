n, k = map(int,input().split())
lst = list(map(int,input().split()))
d = dict()
for num in lst:
    if num not in d:
        d[num]=1
    else:
        d[num]+=1

d_k = list(d.keys())
ans = 0
for num1 in d_k:
    for num2 in d_k:
        for num3 in d_k:
            tmp = [num1,num2,num3]
            if k ==sum(tmp):
                if len(set(tmp))==1 and d[num1]>=3: # 세 수가 모두 같을 때
                    ans += d[num1]*(d[num1]-1)*(d[num1]-2)//6
                elif len(set(tmp))==2: # 두 수가 같을 때
                    if num1==num2 and d[num1]>=2:
                        ans +=d[num1]*(d[num1]-1)*d[num3]//2
                    elif num2==num3 and d[num2]>=2:
                        ans +=d[num2]*(d[num2]-1)*d[num1]//2
                    elif num3==num1 and d[num1]>=2:
                        ans +=d[num3]*(d[num3]-1)*d[num2]//2
                elif len(set(tmp))==3: #모두 다를 때
                    ans += d[num1]*d[num2]*d[num3]//3

print(ans)