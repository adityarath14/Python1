n=5
stars=1
spaces=n-1
for line in range(n):
    print(' '*spaces+'*'*stars)
    spaces-=1
    stars+=2