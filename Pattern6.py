n=7
stars=1
spaces=n//2
for line in range(n//2+1):
    print(' '*spaces+'*'*stars)
    stars+=2
    spaces-=1
stars=n-2
spaces=1
for line in range(n//2):
    print(' '*spaces+'*'*stars)
    stars-=2
    spaces+=1