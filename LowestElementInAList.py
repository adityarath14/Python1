L=[23,56,1,53,55]
minval=L[0]
for ind in range(1,len(L)):
    if L[ind]<minval:
        minval=L[ind]
print(minval)