n=5
stars=n
spaces=0
for line in range(n//2+1):
    print(' '*spaces+'*'*stars)
    stars-=2
    spaces+=1
stars=3
spaces=n//2-1
for line in range(n//2):
    print(' '*spaces+'*'*stars)
    spaces-=1
    stars+=2