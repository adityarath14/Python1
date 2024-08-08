s='ababa'
for sv in range(len(s)):
    for ev in range(sv+1,len(s)+1):
        word=''
        for ind in range(sv,ev):
            word+=s[ind]
        rev=''
        for chr in range(-1,-(len(word)+1),-1):
            rev+=word[chr]
        if word==rev:
            print(word)