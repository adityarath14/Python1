def Outer(arg):
    print(f'arg:{arg}')
    def Inner():
        arg()
    return Inner
@Outer
class M12:
    def __init__(self):
        print('Object Created')
M12()
M12()