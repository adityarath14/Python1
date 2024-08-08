mat=[[1,2,3],[4,5,6],[7,8,9]]
res=[]
for row in range(len(mat)-1,-1,-1):
    line=[]
    for col in range(len(mat)):
        line.append(mat[col][row])
    res.append(line)
print(res)