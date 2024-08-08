class Parent:
    var1=100
    var2=300
    print('Hello')
class Child(Parent):
    var2=200
    var3=400
    print('Hi')
obj1=Parent()
obj2=Child()
print(obj2.var1)