# 1~4
# 1, 22, 333, 4444
beautiful = ['1','22','333','4444']
n = int(input())
total = 0
def make_beauti(answer):
    global total
    if len(answer)==n:
        total+=1
        return
    elif len(answer)>n:
        return
    for s in beautiful:
        make_beauti(answer+s)
    return
make_beauti('')
print(total)