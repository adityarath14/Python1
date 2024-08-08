mat1=[[1,2],[4,5]]
mat2=[[3,4],[1,2]]
if len(mat1)==len(mat2) and len(mat1[0])==len(mat2[0]):
    res=[]
    for row in range(len(mat1)):
        line=[]
        for col in range(len(mat1[0])):
            line.append(mat1[row][col]+mat2[row][col])
        res.append(line)
    print(res)
else:
    print('Addition Not Possible')