lines=5
for row in range(lines):
    for col in range(lines):
        if col==0 or col==lines-1 or row==0 or row==lines-1:
            print('*',end='')
        else:
            print(' ', end='')
    print()