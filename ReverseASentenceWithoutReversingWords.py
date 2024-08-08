str='My Love India'
words=str.split()
ans=[]
for word in range(len(words)-1,-1,-1):
    ans.append(words[word])
print(' '.join(ans))