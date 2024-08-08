num=1
n=5
spaces=2
stars=1
for line in range(n//2+1):
    print(' '*spaces+str(num)*stars)
    num+=1
    spaces-=1
    stars+=2
num=4
stars=n-2
spaces=1
for line in range(n//2):
    print(' '*spaces+str(num)*stars)
    num+=1
    spaces+=1
    stars-=2