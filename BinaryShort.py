L=[0,7,8,11,12,22,420]
user=22
low=0
high=len(L)-1
while low<=high:
    mid=(low+high)//2
    if L[mid]>user:
        high=mid-1
    elif L[mid]<user:
        low=mid+1
    elif L[mid]==user:
        print(mid)
        break
else:
    print(-1)