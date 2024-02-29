global k,n
k,n = map(int,input().split())
def choose(cur_pos):
    if cur_pos == n:
        for num in total_lst:
            print(num, end = ' ')
        print()
        return
    for idx in range(1,k+1):
        total_lst.append(idx)
        choose(cur_pos+1)
        total_lst.pop()

total_lst=[]
choose(0)