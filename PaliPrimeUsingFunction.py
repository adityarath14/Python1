def is_pali(num,dup,ans=0):
    while num!=0:
        ld=num%10
        ans=ans*10+ld
        num//=10
    return dup==ans
def is_Prime(num):
    for fa in range(2,num//2):
        if num%fa==0:
            return False
    return True
num=11
if is_pali(num,num) and is_Prime(num):
    print('Number is ParliPrime')
else:
    print('Number is Not ParliPrime')