s='leeT Code'
res=''
for ind in range(len(s)):
    if 'a'<=s[ind]<='z':
        res+=chr(ord(s[ind])-32)
    else:
        res+=s[ind]
print(res)