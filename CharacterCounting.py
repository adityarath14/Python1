var='aaabbcccccddd'
var+=' '
rev=''
count=1
for ind in range(len(var)-1):
    if var[ind]==var[ind+1]:
        count+=1
    else:
        rev=rev+str(count)+var[ind]
        count=1
print(rev)