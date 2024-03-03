while True:
    s = input()
    if s=='END':
        break
    for alpha in s[::-1]:
        print(alpha, end = '')
    print()