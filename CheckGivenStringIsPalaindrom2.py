s='madam'
for ind in range(len(s)//2+1):
    if s[ind]!=s[-ind-1]:
        print('not palaindrom')
        break
else:
    print('Palaindrom')