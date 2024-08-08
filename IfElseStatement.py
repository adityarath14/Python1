Num1=10000
Num2=15000
Num3=20000
Num4=400000
if Num1>Num2:
    if Num1>Num3:
        if Num1>Num4:
            print(f'{Num1} is Highest')
        else:
            print(f'{Num4} is Highest')
    else:
        if Num3>Num4:
            print(f'{Num3} is higiest')
        else:
            print(f'{Num4} is higiest')
else:
        if Num2>Num3:
            if Num2>Num4:
                print(f'{Num2} is highest')
            else:
                print(f'{Num4} is higiest')
        else:
            if Num3>Num4:
                print(f'{Num3} is Higiest')
            else:
                print(f'{Num4} is Higiest')