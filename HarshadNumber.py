Num=int(input('Enter a Number:'))
copy,res=Num,0
while Num!=0:
    ld=Num%10
    res+=ld
    Num//=10
print('Number is Harshad' if copy%res==0 else 'Number is not Harshad')