import copy
L=[10,20,30,40]
c=copy.copy(L)
print(c)
print(L is c)
print(L[1] is c[1])
L[3]=50
print(L,c)