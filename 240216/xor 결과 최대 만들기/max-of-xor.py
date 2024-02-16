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

def xor(x1,x2): # 두 10진수를 넣고 xor한 10진수를 반환
    x1 =dec2bin(x1)
    x2 = dec2bin(x2)
    # 자릿수 맞춰주기
    max_pos = max(len(x1), len(x2))

    if len(x1)<max_pos:
        x1 = '0'*(max_pos-len(x1))+x1
    if len(x2)<max_pos:
        x2 = '0'*(max_pos-len(x2))+x2
    max_bin = ''
    for pos in range(max_pos):# -> 2개씩 xor
        if x1[pos] != x2[pos]:
            max_bin+='1'
        else: 
            max_bin+='0'
    max_dec = bin2dec(max_bin)
    return max_dec

ans =0
choose = []
def comb(k, cnt):
    global ans
    global choose
    if cnt== m: # 출력
        # print('xor')
        if m==1:
            max_dec = choose[0]
        else:
            for idx in range(m-1):
                tmp = xor(choose[idx], choose[idx+1])
                choose[idx+1] = tmp
            max_dec=choose[-1]
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