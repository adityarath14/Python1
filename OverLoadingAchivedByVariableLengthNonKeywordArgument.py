class M12:
    def method(self,*args):
        res=1
        for var in args:
            res*=var
        print(res)
obj=M12()
obj.method(9,4,3)
obj.method(4)
obj.method(4,3)