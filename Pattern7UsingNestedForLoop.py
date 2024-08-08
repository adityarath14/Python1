var=5
spaces=0
stars=2*var-1
for row in range(var):
    for sp in range(spaces):
        print(' ',end='')
    for st in range(stars):
        print('*',end='')
    spaces+=1
    stars-=2
    print()