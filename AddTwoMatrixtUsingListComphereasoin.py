mat1=[[2,4],[10,3]]
mat2=[[2,5,],[3,6]]
if len(mat1)==len(mat2) and len(mat1[0])==len(mat2[0]):
    res=[[mat1[row][col]+mat2[row][col]for col in range(len(mat1[0]))]for row in range(len(mat1))]
    print(res)
else:
    print('Addition Not Possible')