def prime(num,count=0):
    for var in range(1,num+1):
        if num%var==0:
            count+=1
    if count==2:
        return True
    return False
print(list(map(prime,range(10,41))))