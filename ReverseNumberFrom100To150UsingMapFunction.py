def Reverse(num,ans=0):
    while num!=0:
        ld=num%10
        ans=ans*10+ld
        num//=10
    return ans
print(list(map(Reverse,range(100,151))))