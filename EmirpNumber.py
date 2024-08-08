Num=int(input('Enter a Number:'))
copy,rev=Num,0
while Num!=0:
    ld=Num%10
    rev=rev*10+ld
    Num//=10
if copy!=rev:
    fa_count1=0
    for fa in range(1,copy+1):
        if copy%fa==0:
            fa_count1+=1
    if fa_count1==2:
        fa_count2=0
        for fa in range(1,rev+1):
            if rev%fa==0:
                fa_count2+=1
        if fa_count2==2:
            print('Number is Emirp')
        else:
            print('Number is Not Emirp')
    else:
        print('Number is not Emirp')
else:
    print('Number is not Emirp')