a, b = map(int, input().split())
total = 0
for num in range(a, b+1):
    if num%6==0 and num%8!=0:
        total+=num
print(total)