def Sunny(num,n=0):
    while n*n<=num+1:
        if n*n==num+1:
            return True
        n+=1
num=15
print('Sunny Number' if Sunny(num) else 'Not Sunny Number')