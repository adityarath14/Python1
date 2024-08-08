class p1():
    v1=30
class p2():
    v1=420
class child(p2,p1):
    pass
obj=child()
print(obj.v1)