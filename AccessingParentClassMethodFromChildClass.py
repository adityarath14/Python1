class Parent:
    var1=100
    def Method1(self):
        print('Method1 of parent class')
class Child(Parent):
    var2=200
    def Method2(self):
        print('Method2 of child class')
obj1=Parent()
obj2=Child()
obj2.Method1()