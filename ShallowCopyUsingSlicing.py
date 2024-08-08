L=[50,52,89,78,44]
c=L[::]
print(c)
print(L is c)
print(L[3] is c[3])
L[3]=100
print(L,c)