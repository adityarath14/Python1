def square(num):
    if num==0:
        return 0
    return (num%10)**2+square(num//10)
def cdigit(num):
    if num<=9:
        return num
    return(cdigit(square(num)))
def cHappy(num):
    n=cdigit(num)
    return n==1 or n==7
num=19
print('Happy Number' if cdigit(num) else 'Not Happy Number')