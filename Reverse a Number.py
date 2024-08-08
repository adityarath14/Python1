rev=0
Num=int(input('Enter a number:'))
while Num!=0:
    rem=Num%10
    rev=rev*10+rem
    Num//10
print(Num)