def conqure(Mlist,Llist,Rlist):
    mind,lind,rind=0,0,0
    while lind<len(Llist) and rind<len(Rlist):
        if Llist[lind]>Rlist[rind]:
            Mlist[mind]=Rlist[rind]
            rind+=1
        else:
            Mlist[mind]=Llist[lind]
            lind+=1
        mind+=1
    while lind<len(Llist):
        Mlist[mind]=Llist[lind]
        mind+=1
        lind+=1
    while rind<len(Rlist):
        Mlist[mind]=Rlist[rind]
        mind+=1
        rind+=1
def Divide(L):
    if len(L)>1:
        left,right=L[:len(L)//2],L[len(L)//2:]
        Divide(left)
        Divide(right)
        conqure(L,left,right)
L=[11,44,99,99,11,0]
Divide(L)
print(L)        