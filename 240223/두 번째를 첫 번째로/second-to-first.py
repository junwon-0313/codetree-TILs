s = input()
criteria = s[1]
first = s[0]
new_s = s[:1]
for idx in range(1,len(s)):
    if s[idx] == criteria:
        new_s+= first
    else:
        new_s+=s[idx]
print(new_s)