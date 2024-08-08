def decimal(num,power=0):
    if num==0:
        return 0
    return (num%10)*(2**power)+decimal(num//10,power+1)
num=101010
print(decimal(num))