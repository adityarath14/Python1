def fib(pos):
    if pos==1 or pos==2:
        return pos-1
    return fib(pos-1)+fib(pos-2)
pos=6
print(fib(pos))