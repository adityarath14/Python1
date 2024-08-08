L=[20,55,66,44,66,88]
user=66
def Linear(L,user):
    for ind in range(len(L)):
        if L[ind]==user:
            return ind
    return -1
print(Linear(L,user))