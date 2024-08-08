Num=int(input('Enter a Number:'))
n=0
while n*n<=Num+1:
    if n*n==Num+1:
        print('Sunny Number')
        break
    n+=1
else:
    print('Not Sunny Number')