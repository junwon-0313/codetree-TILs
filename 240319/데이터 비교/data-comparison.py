n = int(input())
arr1 = list(map(int,input().split()))
m = int(input())
arr2 = list(map(int,input().split()))
d = dict()
for k in set(arr1):
    d[k]=1
for num in arr2:
    if num in d:
        print(1, end = ' ')
    else:
        print(0, end =' ')