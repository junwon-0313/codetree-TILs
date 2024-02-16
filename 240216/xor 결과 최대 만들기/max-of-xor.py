n, m = map(int, input().split())
num_lst = list(map(int, input().split()))
# 2진수로 변경 후, xor 연산: 같으먼 0, 다르면 1
def dec2bin(x):
    b = ''
    while True:
        if x<2:
            b+=str(x)
            break
        b+=str(x%2)
        x//=2
    return b[::-1]

def bin2dec(x: str):
    dec = 0
    for idx,num in enumerate(x[::-1]):
        dec+=int(num)*2**idx
    return dec

def xor():
    bin_lst = []
    for num in choose: # 2진수로 변환해서 넣는다. 
        bin_lst.append(dec2bin(num))
    # 자릿수 맞춰주기
    max_pos = max([len(idx) for idx in bin_lst])
    for idx in range(m):
        if len(bin_lst[idx])<max_pos:
            bin_lst[idx] = '0'*(max_pos-len(bin_lst[idx]))+bin_lst[idx]
    max_bin = ''
    for pos in range(max_pos):
        for idx in range(m-1): # 하나라도 다르면 추가
            if bin_lst[idx][pos] != bin_lst[idx+1][pos]:
                max_bin+='1'
                break
        else: # 모두 같으면 0
            max_bin+='0'
            
    max_dec = bin2dec(max_bin[::-1])
    return max_dec

ans =0
choose = []
def comb(k, cnt):
    global ans
    if cnt== m: # 출력
        # print('xor')
        if m==1:
            max_dec = choose[0]
        else:
            max_dec = xor()
        if max_dec >ans:
            ans = max_dec
    if k==n: # 종료 조건
        return
    
    # 그대로 진행
    comb(k+1, cnt)

    # 추가
    choose.append(num_lst[k])   
    comb(k+1,cnt+1)
    choose.pop()

comb(0,0)
print(ans)