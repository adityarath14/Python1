class A1:
    var1=20
class A2(A1):
    var2=30
class A3(A2):
    var3=40
obj=A3()
print(obj.var3,obj.var2,obj.var1)