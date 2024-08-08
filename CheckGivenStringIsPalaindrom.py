s='madam'
for ind in range(len(s)//2):
    if s[ind]!=s[len(s)-1-ind]:
        print('Not Palaindrom')
        break
else:
    print('Palaindrom')