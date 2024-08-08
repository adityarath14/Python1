class M12:
    def method(self,var1,var2):
        print(var1*var2)
    def method(self,var1,var2,var3):
        print(var1*var2*var3)
    def method(self,var1,var2,var3,var4):
        print(var1*var2*var3*var4)
obj=M12()
obj.method(2,3,1)
#To make overloading possible we need variable length nonkeyword argument.