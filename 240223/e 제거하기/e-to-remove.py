s = input()
new_s = ''
first_e=1000
for idx, w in enumerate(s):
    if w =='e':
        first_e=idx
        break
        
print(s[:idx]+s[idx+1:])