Num=int(input('Enter Your Number:'))
while Num>9:
    d_sum=0
    while Num!=0:
        ld=Num%10
        d_sum+=ld**2
        Num//=10
    Num=d_sum
if Num==1 or Num==7:
    print('Number is Happy Number')
else:
    print('Number is not Happy Number')