def fib(pos):
    f=0
    s=1
    for _ in range(pos):
        t=f+s
        yield f
        f,s=s,t
pos=4
obj=fib(pos)
#print(list(obj))
print(next(obj))
print(next(obj))
print(next(obj))
print(next(obj))