def Fact(num):
    if num==0 or num==1:
        return 1
    return num*Fact(num-1)
def digit(num):
    if num==0:
        return 0
    return Fact(num%10)+digit(num//10)
def cSpecial(num):
    return num==digit(num)
num=40585
print('Special Number' if cSpecial(num) else 'Not Special Number')