L=[7,2,3,8,1,5,6]
target=8
for ind1 in range(len(L)):
    for ind2 in range(ind1+1,len(L)):
        if L[ind1]+L[ind2]==target:
            print(L[ind1],L[ind2])