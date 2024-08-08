def Niv(num,dsum=0):
    while num!=0:
        ld=num%10
        dsum+=ld
        num//=10
    return dsum
def cNiv(num):
    if num%Niv(num)==0:
        return True
num=156
print('Harshad Number' if cNiv(num) else 'Not Harshad Number')