A = input()
# 최대한 같은 수가 이어지면 #달라지는 횟수를 구함
ans =100
for shift in range(1, len(A)):
    tmp_A = A[shift:] + A[:shift]
    total =''
    cnt =1
    x = tmp_A[0]
    for nx in range(1, len(A)):
        if x!=tmp_A[nx]:
            total+=x
            total+=str(cnt)
            x = tmp_A[nx]
            cnt =1
        else:
            cnt+=1
    total+= x
    total+=str(cnt)
    # print(total)
    if len(total)<ans:
        ans=len(total)

print(ans)