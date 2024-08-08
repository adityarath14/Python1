L=[62,93,56,85,25,20]
user=28
def Linear(L,user,ind=0):
    if ind==len(L):
        return -1
    if L[ind]==user:
        return ind
    return Linear(L,user,ind+1)
print(Linear(L,user))