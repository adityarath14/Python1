def comp(Num):
    for var in range(2,int(Num**0.5)+1):
        if Num%var==0:
            return 'composite'
    return 'Not Composite'
print(comp(9))