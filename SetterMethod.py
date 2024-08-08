class access:
    def __init__(self):
        self.__a=420
    def getter(self):
        return self.__a
    def setter(self,value):
        self.__a=value
obj=access()
print(obj.getter())
obj.setter(840)
print(obj.getter())