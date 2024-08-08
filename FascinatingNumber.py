Num=int(input('Enter a Number:'))
check=str(Num*1)+str(Num*2)+str(Num*3)
for var in range(1,10):
    if str(var) not in check:
        print('Number is not Facinating')
        break
else:
    print('Number is Facinating')