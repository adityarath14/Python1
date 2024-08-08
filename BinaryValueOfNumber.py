Num=int(input('Enter a Number:'))
ans=0
pos=1
while Num!=0:
    rem=Num%2
    ans=ans+(rem*pos)
    pos*=10
    Num//=2
print(ans)