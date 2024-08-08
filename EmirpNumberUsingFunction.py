def prime(num):
    for fa in range(2,num//2+1):
        if num%fa==0:
            return False
    return True
def rev(num,sol=0):
    while num!=0:
        ld=num%10
        sol=sol*10+ld
        num//=10
    return sol
num=13
revnum=rev(num)
if (num!=revnum) and (prime(num)) and (prime(revnum)):
    print('Emirp Number')
else:
    print('Not Emirp Number')