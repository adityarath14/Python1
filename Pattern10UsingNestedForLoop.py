var=5
num=var
for line in range(1,var+1):
    for column in range(line):
        print(num,end='')
    num-=1
    print()