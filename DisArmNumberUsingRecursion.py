def Disarm(num,power):
    if num==0:
        return 0
    return (num%10)**power+Disarm(num//10,power-1)
num=135
print('Disarm Number' if num==Disarm(num,len(str(num))) else 'Not Disarm Number')