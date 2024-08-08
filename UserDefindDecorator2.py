def Outer(arg):
    print(f'arg:{arg}')
    def inner():
        arg()
        print('Inside Inner Function')
    return inner
@Outer
def m1():
    print('inside m1')
m1()
print(f'm1:{m1}')