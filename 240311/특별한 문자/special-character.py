lst = list(input())
d= dict()

for letter in lst:
    if letter in d:
        d[letter]+=1
    else:
        d[letter]=1

ans_lst = []
for k,v in d.items():
    if v==1:
        ans_lst.append(k)

for letter in lst:
    if letter in ans_lst:
        print(letter)
        break