L=[25,66,52,98,56]
maxval=L[0]
for ind in range(1,len(L)):
    if L[ind]>maxval:
        maxval=L[ind]
print(maxval)