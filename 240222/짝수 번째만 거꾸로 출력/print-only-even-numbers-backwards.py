sentence = input()
ans = ''
for idx, letter in enumerate(sentence):
    if (idx+1)%2==0:
        ans+=letter

print(ans[::-1])