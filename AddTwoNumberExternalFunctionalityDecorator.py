def Outer(arg):
    def Inner(a,b):
        if a<0:
            a=a*(-1)
        if b<0:
            b=b*(-1)
        arg(a,b)
    return Inner
@Outer
def sum(val1,val2):
    print(val1+val2)
sum(5,2)
sum(2,-5)
sum(-2,5)