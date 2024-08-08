d={}
n1=int(input('Enter a Number:'))
n2=int(input('Enter another Number'))
try:
    print(n1/n2)
    d[['a',5,7]]=56
    print(d)
except ZeroDivisionError:
    print('Can not divide by zero')
except TypeError:
    print('unhasable Type')