lines=5
for row in range(lines):
    for column in range(lines):
        if row==column or row+column==lines-1:
            print('*',end='')
        else:
            print(' ',end='')
    print()