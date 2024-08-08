def Armstrong(num,power):
    if num==0:
        return 0
    return (num%10)**power+Armstrong(num//10,power)
num=153
print('Armstrong Number' if num==Armstrong(num,len(str(num))) else 'Not Armstrong Number')