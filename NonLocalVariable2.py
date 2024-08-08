def outer():
    var=30
    print(f'nonlocal space:{var}')
    def inner():
        nonlocal var
        var=50
        print(f'local space:{var}')
    inner()
    print(f'nonlocal space:{var}')
outer()
#print(f'Global space:{var}')