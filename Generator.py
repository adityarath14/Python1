def A():
    a=20
    yield a
    a+=10
    yield a
obj=A()
print(next(obj))
print(next(obj))
#print(next(obj))