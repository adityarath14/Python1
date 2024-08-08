L=[22,56,10,45,2]
for ind1 in range(len(L)-1):
    low=ind1
    for ind2 in range(ind1+1,len(L)):
        if L[low]>L[ind2]:
            low=ind2
    L[ind1],L[low]=L[low],L[ind1]
print(L)