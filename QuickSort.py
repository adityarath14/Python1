def Quick(var):
    if len(var)<=1:
        return var
    pivot=var[0]
    low=[var[ind] for ind in range(1,len(var)) if pivot>var[ind]]
    high=[var[ind] for ind in range(1,len(var)) if pivot<=var[ind]]
    return Quick(low)+[pivot]+Quick(high)
var=[17,-12,99,111,2,-3,-420]
print(Quick(var))