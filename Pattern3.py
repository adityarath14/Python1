n=5
stars=n
spaces=0
for line in range(n):
    print(' '*spaces+'*'*stars)
    spaces+=1
    stars-=1