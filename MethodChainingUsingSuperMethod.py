class V1():
    var1=100
    def Method1(self):
        print('Method1 Of Parent class')
class V2(V1):
    var2=200
    def Method2(self):
        print('Method2 Of parent class')
        super().Method1()
obj1=V1()
obj2=V2()
obj2.Method2()