def square(num,dsum=0):
    while num!=0:
        ld=num%10
        dsum+=ld**2
        num//10
    return dsum
def cHappy(num):
    while num>9:
        num=square(num)
    return num==1 or num==7
num=19
print('Happy Number' if cHappy(num) else 'Not Happy Number')