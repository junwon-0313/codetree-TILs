lst = list(input())

ans =0
for idx in range(len(lst)):
    if lst[idx]=='(':
        cnt=0
        for idx2 in range(idx+1, len(lst)):
            if lst[idx2]==')':
                cnt+=1
        ans+= cnt
print(ans)