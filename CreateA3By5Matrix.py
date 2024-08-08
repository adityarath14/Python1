rows=3
cols=5
mat=[]
for row in range(rows):
    line=[]
    for col in range(cols):
        line.append(int(input('enter the values:')))
    mat.append(line)
print(mat)