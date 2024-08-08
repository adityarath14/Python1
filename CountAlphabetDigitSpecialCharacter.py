s='we aRe 6 Future @420 developer & moye moye'
alphacount,digcount,spcount=0,0,0
for ch in s:
    if 'A'<=ch<='Z' or 'a'<=ch<='z':
        alphacount+=1
    elif '0'<=ch<='9':
        digcount+=1
    else:
        spcount+=1
print(alphacount,digcount,spcount)