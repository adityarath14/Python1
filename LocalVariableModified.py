def Sample():
    global var
    var-=11
    print(f'Local Space:{var}')
var=420
Sample()
print(f'Global Space:{var}')