var='I Love My India'
words=var.split()
result=[]
for word in words:
    rev=''
    for ind in range(len(word)-1,-1,-1):
        rev+=word[ind]
    result.append(rev)
print(' '.join(result))