s='mock'
for sv in range(len(s)):
    for ev in range(sv+1,len(s)+1):
        word=''
        for ind in range(sv,ev):
            word+=s[ind]
        print(word)