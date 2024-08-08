def c_Armstrong(num,dup,n_digit,sol=0):
    while num!=0:
        ld=num%10
        sol+=ld**n_digit
        num//=10
    return dup==sol
num=111
print('Armstrong Number' if c_Armstrong(num,num,len(str(num))) else 'Not Armstrong Number')