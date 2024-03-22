x, y = map(int,input().split())
ans =0
for num in range(x,y+1):
    if str(num)[::-1] == str(num):
        ans+=1
print(ans)