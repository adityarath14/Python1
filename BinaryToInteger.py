Num=10110
ans=0
pow=0
while Num!=0:
    ld=Num%10
    ans=ans+ld*(2**pow)
    pow+=1
    Num//=10
print(ans)