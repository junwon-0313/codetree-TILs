n = int(input())
cnt =1
total = 0
while True:
    if n<=1:
        print(total)
        break
    n //= cnt
    cnt+=1
    total+=1