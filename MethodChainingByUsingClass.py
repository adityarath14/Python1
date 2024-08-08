class V1:
    var1=100
    def Method1(self):
        print('Method1 of parent class')
    def Method3(self):
        print('Method3 of parent class')
class V2(V1):
    var2=200
    def Method1(self):
        print('Method1 of child class')
        V1.Method3(self)
obj1=V1()
obj2=V2()
obj2.Method1()