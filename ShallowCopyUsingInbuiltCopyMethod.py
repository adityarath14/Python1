L=[44,55,66,77]
c=L.copy()
print(c)
print(L is c)
print(L[0] is c[0])
L[0]=500
print(L[0] is c[0])
print(L,c)