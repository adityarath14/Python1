var=4
spaces=0
stars=var
for line in range(var):
    for sp in range(spaces):
        print(' ',end='')
    for st in range(stars):
        print(stars,end='')
    spaces+=1
    stars-=1
    print()