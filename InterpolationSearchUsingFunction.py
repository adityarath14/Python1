def interpolation(L,user):
    low=0
    high=len(L)-1
    while low<=high and L[low]<=user<=L[high]:
        ind=int(low+((low-high)/(L[low]-L[high]))*(user-L[low]))
        if L[ind]>user:
            high=ind-1
        elif L[ind]<user:
            low=ind+1
        elif L[ind]==user:
            return ind
    return -1
L=[10,22,25,49,53,420]
user=53
print(interpolation(L,user))