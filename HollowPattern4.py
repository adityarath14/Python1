lines=5
spaces=0
for line in range(lines,0,-1):
    for sp in range(spaces):
        print(' ',end='')
    for st in range(line):
        if line==lines or st==0 or st==line-1:
            print('*',end='')
        else:
            print(' ',end='')
    print()
    spaces+=1