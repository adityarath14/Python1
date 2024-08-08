s='My name is Aditya'
word=s.split()
ans=[]
for ind in range(len(word)-1,-1,-1):
    ans.append(word[ind])
print(' '.join(ans))
