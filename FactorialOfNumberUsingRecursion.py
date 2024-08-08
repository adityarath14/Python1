def Fact(sv,num):
    if sv==num:
        return num
    return num*Fact(sv+1,num)
sv=1
num=2
print(Fact(sv,num))