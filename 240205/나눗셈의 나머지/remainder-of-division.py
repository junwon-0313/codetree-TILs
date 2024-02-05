a, b = map(int, input().split())
lst = [0]*b
while True:
    if a<b:
        break
    r = a%b
    lst[r]+=1
    a //=b

answer = 0
for cnt in lst:
    answer+= cnt**2
print(answer)