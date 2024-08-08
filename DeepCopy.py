from copy import deepcopy
L=[[89,99,79,69],[20,10,80]]
c=deepcopy(L)
print(L is c)
print(L[0] is c[0])
L[0][0]=55
print(L,c)