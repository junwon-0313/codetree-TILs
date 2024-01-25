a = int(input())

lst_bcde =list(map(int, input().split()))

for i in lst_bcde:
    if a>i:
        print(1)
    else:
        print(0)