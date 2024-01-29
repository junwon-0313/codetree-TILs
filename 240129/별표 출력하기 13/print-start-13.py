n = int(input())
lst = []
if n==1:
    lst =[1,1]
elif n==2:
    lst =[2,1,1,2]
else:
    lst.append(n)
    lst.append(1)
    for num in range(n-1,1,-1):
        lst.append(num)
    for num in range(2,n):
        lst.append(num)
    lst.append(1)
    lst.append(n)

for i in lst:
    print('* '*i)