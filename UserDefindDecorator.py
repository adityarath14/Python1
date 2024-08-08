def outer(arg):
    print(f'arg:{arg}')
    def inner():
        arg()
        print('Inside Inner Function')
    return inner
@outer
def function():
    print('Inside Function')
function()