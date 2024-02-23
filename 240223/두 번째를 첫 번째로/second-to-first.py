s = input()
criteria = s[1]
first = s[0]
for idx in range(2,len(s)):
    if s[idx] == criteria:
        s[idx]=first
print(s)