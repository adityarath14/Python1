lines=5
for line in range(1,lines+1):
    for star in range(line):
        if star==0 or line==lines or star==line-1:
            print('*',end='')
        else:
            print(' ',end='')
    print()