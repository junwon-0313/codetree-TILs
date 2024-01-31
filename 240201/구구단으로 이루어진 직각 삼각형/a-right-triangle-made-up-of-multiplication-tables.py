n = int(input())

for i in range(n):
    for j in range(1,n-i):
        print(f'{i+1} * {j} = {(i+1)*j}', end =' / ')
    print(f'{i+1} * {n-i} = {(i+1)*(n-i)}')