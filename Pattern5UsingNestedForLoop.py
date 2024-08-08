var=5
spaces=0
stars=var
for row in range(var):
    for sp in range(spaces):
        print(' ',end='')
    for st in range(stars):
        print('*',end='')
    spaces+=1
    stars-=1
    print()