def prime(num,count=0):
    for fa in range(1,num+1):
        if num%fa==0:
            count+=1
    if count==2:
        return True
print(list(filter(prime,range(100,1001))))