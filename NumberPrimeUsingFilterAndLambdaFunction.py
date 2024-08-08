num=11
print('Not Prime Number'if list(filter(lambda fa:num%fa==0,range(2,num//2+1))) else 'Prime Number')