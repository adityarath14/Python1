L1=list(map(int,input().split()))
print(L1)
L2=list(map(int,input().split()))
print(L2)
res=[]
for ind in range(len(L1)):
    res.append(L1[ind]+L2[ind])
print(res)