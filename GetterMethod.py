class access:
    def __init__(self):
        self.__a=420
    def getter(self):
        return self.__a
obj=access()
print(obj.getter())