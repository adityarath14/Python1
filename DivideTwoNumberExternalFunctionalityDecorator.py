def Outer(arg):
    def Inner(a,b):
        arg(b,a) if b==0 else arg(a,b)
    return Inner
@Outer
def div(val1,val2):
    print(val1/val2)
div(0,3)
div(3,0)