def Outer():
    var=30
    print(f'nonlocal space:{var}')
    def inner():
        print(f'local space:{var}')
    inner()
Outer()
#print(f'Global space:{var}')