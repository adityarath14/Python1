def Fact(num,fa=1):
    if fa==num:
        return num
    return fa*Fact(num,fa+1)
def Armsrtrong(num,res=0):
    dup=num
    n_digit=len(str(num))
    while num!=0:
        rem=num%10
        res+=rem**n_digit
        num//=10
    return dup==res
def palaindrom(num,rev=0):
    dup=num
    while num!=0:
        rem=num%10
        rev=rev*10+rem
        num//=10
    return dup==rev
babai=420
print(__name__)
if __name__=='__main__':
    print(Fact(5))