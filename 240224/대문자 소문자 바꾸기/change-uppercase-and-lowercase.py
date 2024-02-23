s = input()

for t in s:
    if t.isupper():
        print(t.lower(), end ='')
    else:
        print(t.upper(), end ='')