lines=5
spaces=lines-1
for line in range(1,lines+1):
    for sp in range(spaces):
        print(' ',end='')
    for st in range(line):
        if st==0 or line==lines or st==line-1:
            print('*',end='')
        else:
            print(' ',end='')
    print()
    spaces-=1