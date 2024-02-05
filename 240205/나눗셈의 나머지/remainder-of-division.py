a, b = map(int, input().split())
lst = [0]*b
while True:
    r = a%b
    lst[r]+=1
    a //=b
    if a==0:
        break

answer = 0
for cnt in lst:
    answer+= cnt**2
print(answer)