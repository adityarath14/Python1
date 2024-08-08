def fact(n):
    res=1
    for fa in range(1,n+1):
        res*=fa
        yield res
ob=fact(5)
#print(list(ob))
'''for li in ob:
    print(li)'''
'''while True:
    print(next(ob))'''
print(next(ob))
print(next(ob))
print(next(ob))
print(next(ob))
print(next(ob))