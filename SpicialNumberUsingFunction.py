def fact(num,mul=1):
    for var in range(1,num+1):
        mul*=var
    return mul
def is_digit(num,copy,d_sum=0):
    while num!=0:
        ld=num%10
        d_sum+=fact(ld)
        num//=10
    return copy==d_sum
def Special(num):
    return is_digit(num,num)
num=145
print('Special Number' if Special(num) else 'Not Special Number')