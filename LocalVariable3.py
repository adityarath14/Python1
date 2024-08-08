def Outer():
    print(f'Non Local Space:{var}')
    def  Inner():
        print(f'Local Space:{var}')
    Inner()
var=30
Outer()
print(f'Global Space:{var}')