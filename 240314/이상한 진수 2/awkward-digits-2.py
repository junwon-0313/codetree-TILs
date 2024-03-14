def bin2dec(s):
    dec = 0
    cnt=0
    for num in s[::-1]:
        dec+=int(num)*2**cnt
        cnt+=1
    return dec
s = input()
ans =0
for idx in range(len(s)): #모든 자리에서 숫자를 하나씩 바꿔보며 최댓값을 구한다.
    tmp =''
    for i in range(len(s)):
        if i==idx:
            if s[i]=='0':
                tmp+='1'
            else:
                tmp+='0'
        else:
            tmp+=s[i]
    new = bin2dec(tmp)
    if new > ans:
        ans = new
print(ans)