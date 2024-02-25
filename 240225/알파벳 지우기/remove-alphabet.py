a = input()
b = input()
num1 = ''
num2 = ''
for s in a:
    if '0'<=s<='9':
        num1+=s
for s in b:
    if '0'<=s<='9':
        num2+=s
print(int(num1)+int(num2))