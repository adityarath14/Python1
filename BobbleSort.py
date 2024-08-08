L=[5,22,80,56,9,20]
for ind1 in range(len(L)-1,0,-1):
    for ind2 in range(ind1):
        if L[ind2]>L[ind2+1]:
            L[ind2],L[ind2+1]=L[ind2+1],L[ind2]
print(L)