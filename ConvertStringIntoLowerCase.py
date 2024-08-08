s='Leet CoDe'
res=''
for ind in range(len(s)):
    if 'A'<=s[ind]<='Z':
        res+=chr(ord(s[ind])+32)
    else:
        res+=s[ind]
print(res)