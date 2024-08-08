var=4
spaces=var-1
stars=1
for line in range(var):
    for sp in range(spaces):
        print(' ',end='')
    for st in range(stars):
        print(line+1,end='')
    spaces-=1
    stars+=1
    print()