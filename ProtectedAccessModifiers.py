class access:
    def __init__(self):
        self._a=420
    def M1(self):
        print(self._a)
obj=access()
obj.M1()
print(obj._a)