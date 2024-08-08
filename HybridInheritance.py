class A():
    var=10
class B(A):
    var2=20
class C(A):
    var1=30
class D(B,C):
    pass
obj=D()
print(obj.var)