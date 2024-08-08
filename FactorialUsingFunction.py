def fact(Num):
    Res=1
    for n in range(1,Num+1):
        Res*=n
    return Res
print(fact(5))