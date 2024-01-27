lst =[int(input()) for _ in range(5)]
for i in lst:
    if i %3!=0:
        print(0)
        break
else:
    print(1)