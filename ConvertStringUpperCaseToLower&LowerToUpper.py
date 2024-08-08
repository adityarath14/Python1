s='LeEt CoDe'
res=''
for ind in range(len(s)):
    if 'A'<=s[ind]<='Z':
        res+=chr(ord(s[ind])+32)
    elif 'a'<=s[ind]<='z':
        res+=chr(ord(s[ind])-32)
print(res)