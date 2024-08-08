def c_Disarm(num,dup,n_digit,sol=0):
    while num!=0:
        ld=num%10
        sol+=ld**n_digit
        n_digit-=1
        num//=10
    return dup==sol
num=135
print('Disarm Number' if c_Disarm(num,num,len(str(num))) else 'Not Disarm Number')