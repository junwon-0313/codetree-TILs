# 4**6*200
sentence = input()

operator = []
operand = []
for x in sentence:
    if x in ['+','-','*']:
        operator.append(x)
    else:
        operand.append(x)
# print(operator)

# 1 1 1
def choose(k):
    if len(lst)==k:
        calc(lst)
        return
    
    for idx in range(1,5):
        lst.append(idx)
        choose(k)
        lst.pop()

oper_lst = list(set(operand))
oper_lst.sort()

def calc(lst):
    global total
    d = dict()
    cnt=0
    for k in oper_lst:
        d[k]=lst[cnt]
        cnt+=1
    ans = d[sentence[0]]
    for idx, s in enumerate(sentence):
        if idx%2==1:
            if sentence[idx]=='+':
                ans +=d[sentence[idx+1]]
            elif sentence[idx]=='-':
                ans -=d[sentence[idx+1]]
            elif sentence[idx]=='*':
                ans *=d[sentence[idx+1]]
    total = max(total, ans)

total =-1e9
lst = []
choose(len(set(operand)))
print(total)