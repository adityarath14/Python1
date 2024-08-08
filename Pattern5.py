n=4
stars=2*n-1
spaces=0
for line in range(5):
    print(' '*spaces+'*'*stars)
    stars-=2
    spaces+=1