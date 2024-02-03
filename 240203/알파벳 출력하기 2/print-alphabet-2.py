n = int(input())
lst = [chr(i) for i in range(65,91)]

cnt = 0
for idx in range(n):
    print('  '*idx, end = '')
    for _ in range(n-idx):
        print(lst[cnt], end = ' ')
        cnt= (cnt+1)%24
    print()