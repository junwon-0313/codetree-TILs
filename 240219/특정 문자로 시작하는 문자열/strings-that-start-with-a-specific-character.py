n = int(input())
lst = [input() for _ in range(n)]
target = input()
total_l = 0
cnt = 0
for word in lst:
    if word[0]==target:
        cnt+=1
        total_l+=len(word)

print(f'{cnt} {(total_l/cnt):.2f}')