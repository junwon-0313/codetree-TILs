a, b = map(int, input().split())
for mul in [2,4,6,8]:
    for i in range(b,a,-1):
        print(f'{i} * {mul} = {i*mul}', end = ' / ')
    print(f'{a} * {mul} = {a*mul}')