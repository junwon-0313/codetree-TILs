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
    for num in choose:
        bin_lst.append(dec2bin(num))
    # 자릿수 맞춰주기
    max_pos = max(len(bin_lst[0]), len(bin_lst[1]), len(bin_lst[2]))
    for idx in range(3):
        if len(bin_lst[idx])<max_pos:
            bin_lst[idx] = '0'*(max_pos-len(bin_lst[idx]))+bin_lst[idx]
    max_bin = ''
    for pos in range(max_pos):
        if bin_lst[0][pos] == bin_lst[1][pos] == bin_lst[2][pos]: # 다 같을 경우
            max_bin+='0'
        else:
            max_bin+='1'
    max_dec = bin2dec(max_bin)
    return max_dec

ans =0
choose = []
def comb(k, cnt):
    global ans
    if cnt==3: # 출력
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