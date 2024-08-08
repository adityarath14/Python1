lines=5
for line in range(lines,0,-1):
    for st in range(line):
        if line==lines or st==0 or st==line-1 :
            print('*',end='')
        else:
            print(' ',end='')
    print()