s='MADAM'
rev=''
for ind in range(-1,-len(s)-1,-1):
    rev+=s[ind]
print('Palaindrom' if rev==s else 'Not Palaindrom')