n=8
stars=n
spaces=0
for i in range(n):
    print('*'*stars+' '*spaces)
    spaces+=1
    stars-=1