var=5
spaces=var-1
stars=1
for row in range(var):
    for sp in range(spaces):
        print(' ',end='')
    for st in range(stars):
        print('*',end='')
    stars+=2
    spaces-=1
    print()