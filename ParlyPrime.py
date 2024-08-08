Num=int(input('Enter a Number:'))
copy,rev=Num,0
while Num!=0:
    ld=Num%10
    rev=rev*10+ld
    Num//=10
if copy==rev:
        fa_count=0
        for fa in range(1,copy+1):
            if copy%fa==0:
                fa_count+=1
        if fa_count==2:
            print('Number is ParlyPrime')
        else:
            print('Number is not ParlyPrime')
else:
    print('Number is not ParlyPrime')