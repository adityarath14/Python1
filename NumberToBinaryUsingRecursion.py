def Bin(num,pos=1):
    if num==0:
        return 0
    return (num%2)*Bin(num//2,pos*10)
num=20
print(Bin(num))