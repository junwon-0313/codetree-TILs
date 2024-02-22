a = input()
b = input()
total = 0
for idx in range(len(a)):
    if a[idx:idx+2]==b:
        total+=1
print(total)