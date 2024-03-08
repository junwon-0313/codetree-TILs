lst = []
while True:
    s = input()
    if s=='0':
        break
    lst.append(s)
print(len(lst))
for idx in range(len(lst)):
    if (idx+1)%2==1:
        print(lst[idx])